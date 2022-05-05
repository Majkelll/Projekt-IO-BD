from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from .models import User, BMI
from . import db
from flask_login import login_user, current_user, logout_user
from passlib.hash import sha256_crypt
from datetime import datetime
from website.scripts.auth.signup.validation import validate_data
from website.scripts.consts.login_messages import *
from website.scripts.bmi.bmi_bmr_calculator import calculate_bmi, calculate_bmr
from website.scripts.bmi.bmi_summary import bmi_summary
from website.scripts.bmi.validation import validate_bmi_form
from website.scripts.utilities.birthdate_to_age import calculate_age

views = Blueprint("views", __name__)


@views.route('/')
def home():
    return render_template('./home/home.html')

@views.route('/bmi/data', methods=['POST'])
def bmi_data():
    if current_user.is_authenticated:
        bmi = BMI.query.filter_by(user_id=current_user.id).all()
        result = []
        for k in bmi:
            result.append({
                'height': float(k.height),
                'weight': float(k.weight),
                'date': k.data_collected
            })

        if len(result) > 0:
            return jsonify(result)
        else:
            return '{}'
    else:
        return 'User does not exist'

@views.route('/bmi', methods=['GET', 'POST'])
def bmi():
    bmi = None
    bodytype_summary = None
    bmr = None
    if request.method == 'POST':
        weight = request.form.get('weight')
        height = request.form.get('height')
        gender = request.form.get('gender') if not current_user.is_authenticated else current_user.gender
        birthdate = datetime.strptime(request.form.get('birthdate'), '%Y-%m-%d').date() if not current_user.is_authenticated else current_user.birthdate

        validate = validate_bmi_form(weight, height, birthdate, gender)
        if validate['status'] == 'success':
            weight = float(weight)
            height = float(height)
            age = calculate_age(birthdate)
            bmi = calculate_bmi(weight, height)
            bmr = calculate_bmr(gender, weight, height, age)
            bodytype_summary = bmi_summary(bmi)

            if current_user.is_authenticated:
                new_measurement = BMI(user_id=current_user.id, weight=weight, height=height)
                db.session.add(new_measurement)
                db.session.commit()
        else:
            flash(validate['content'], category=validate['status'])

    return render_template('./bmi/bmi.html', bmi=bmi, summary=bodytype_summary, bmr=bmr)


@views.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':

        email = request.form.get('email')
        first_name = request.form.get('firstName')
        passwords = [request.form.get('password1'), request.form.get('password2')]
        birthdate = datetime.strptime(request.form.get('birthdate'), '%Y-%m-%d')
        gender = request.form.get('gender')

        validate = validate_data(email, first_name, passwords[0], passwords[1], birthdate, gender)

        if validate['status'] == 'error':
            flash(validate['content'], category=validate['status'])
        elif validate['status'] == 'success':
            hashed_password = sha256_crypt.encrypt(passwords[0])
            new_user = User(email=email, username=first_name, password=hashed_password, gender=gender, birthdate=birthdate)
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


@views.route('/logout', methods=['GET', 'POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect('/login')
