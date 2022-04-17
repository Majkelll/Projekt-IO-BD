from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_mail import Mail

from website.scripts.consts.email import EMAIL_ADDRESS, EMAIL_PASSWORD

db = SQLAlchemy()
DB_NAME = "database.db"
mail = Mail()


def create_app():
    app = Flask(__name__, static_folder='./static')
    app.config['SECRET_KEY'] = "gflgkdfgdfgogsdfksdflsdsfkgekh"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # email set up
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = EMAIL_ADDRESS
    app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)

    # db init
    db.init_app(app)

    # blue prints
    from .views import views
    app.register_blueprint(views, url_prefix="/")

    # models
    from .models import User

    # database startup
    create_database(app)

    # login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("[DB] Created database")
