from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__, static_folder='./static')
    app.config['SECRET_KEY'] = "gflgkdfgdfgogsdfksdflsdsfkgekh"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

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
