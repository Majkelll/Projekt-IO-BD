from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

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

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("[DB] Created database")
