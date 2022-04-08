from flask import Blueprint, render_template, request, redirect, url_for, flash

from website.scripts.helpers import send_email
from .models.User import User
from . import db
from flask_login import login_user
from passlib.hash import sha256_crypt
from website.scripts.auth.signup.validation import validate_data
from website.scripts.consts.login_messages import *

views = Blueprint("views", __name__)


@views.route('/')
def home():
    return render_template('./home/home.html')


@views.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        passwords = [request.form.get(
            'password1'), request.form.get('password2')]

        validate = validate_data(email, first_name, passwords[0], passwords[1])

        if validate['status'] == 'error':
            flash(validate['content'], category=validate['status'])
        elif validate['status'] == 'success':
            hashed_password = sha256_crypt.encrypt(passwords[0])
            new_user = User(email=email, username=first_name,
                            password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash(validate['content'], category=validate['status'])

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
            else:
                flash(WRONG_PASSWORD, category="error")
        else:
            flash(WRONG_EMAIL, category="error")

    return render_template('./login/login.html')
