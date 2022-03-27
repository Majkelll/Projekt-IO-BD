from flask import Blueprint, render_template, request

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
    return render_template('./signup/signup.html')


@views.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('./login/login.html')
