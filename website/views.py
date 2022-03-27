from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from . import db
from flask_login import login_user

views = Blueprint("views", __name__)


@views.route('/')
def home():
    return render_template('./home/home.html')


@views.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        passwords = [request.form.get(
            'password1'), request.form.get('password1')]
        new_user = User(email=email, username=firstName, password=passwords[0])
        db.session.add(new_user)
        db.session.commit()
    return render_template('./signup/signup.html')


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                login_user(user, remember=True)
                return redirect(url_for('views.home'))

    return render_template('./login/login.html')
