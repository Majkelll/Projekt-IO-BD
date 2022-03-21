from flask import Flask
from .views import views


def create_app():
    app = Flask(__name__, static_folder='./static')

    # register blueprints
    app.register_blueprint(views, url_prefix="/")

    return app
