from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route('/')
def home():
    return render_template('./home/home.html')

@views.route('/signup')
def signup():
    return render_template('./signup/signup.html')

@views.route('/login')
def login():
    return render_template('./login/login.html')

