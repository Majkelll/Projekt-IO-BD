from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from . import db
from flask_login import login_user
from passlib.hash import sha256_crypt
import re


def check_email(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return re.fullmatch(regex, email)


def check_password(password):
    min_length = 8
    uppercase = True
    lowercase = True
    numbers = True
    special_characters = True

    # check length
    if len(password) < min_length:
        return False
    # look for uppercase
    if uppercase and re.search(r"[A-Z]", password) is None:
        return False
    # look for lowercase
    if lowercase and re.search(r"[a-z]", password) is None:
        return False
    # look for digits
    if numbers and re.search(r"\d", password) is None:
        return False
    #look for special characters
    if special_characters and re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None:
        return False

    return True


views = Blueprint("views", __name__)


@views.route('/')
def home():
    return render_template('./home/home.html')


@views.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':

        wrong_data = False

        email = request.form.get('email')
        first_name = request.form.get('firstName')
        passwords = [request.form.get(
            'password1'), request.form.get('password2')]

        # check if email correct
        if not check_email(email):
            flash("Nieprawidłowy email.", category="error")
            wrong_data = True

        # check username
        elif len(first_name) < 2:
            flash("Wpisz poprawne imię.", category="error")
            wrong_data = True

        # check if password the same
        elif passwords[0] != passwords[1]:
            flash("Wpisane hasła nie są identyczne.", category="error")
            wrong_data = True

        # check password
        elif not check_password(passwords[0]):
            flash("Hasło musi składać się z co najmniej 8 znaków i musi zawierać: duże i małe litery, cyfry i znaki specjalne.", category="error")
            wrong_data = True

        if not wrong_data:
            hashed_password = sha256_crypt.encrypt(passwords[0])
            new_user = User(email=email, username=first_name, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("Konto zostało utworzone. Możesz teraz się zalogować.", category="success")

    return render_template('./signup/signup.html')


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if sha256_crypt.verify(password, user.password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))

    flash("Wprowadzono błędne dane logowania.", category="error")
    return render_template('./login/login.html')
