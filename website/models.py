from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.schema import ForeignKey


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    gender = db.Column(db.String(1))
    birthdate = db.Column(db.Date)
    data_created = db.Column(db.DateTime(timezone=True), default=func.now())


class BMI(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    weight = db.Column(db.Numeric)
    height = db.Column(db.Numeric)
    data_collected = db.Column(db.DateTime(timezone=True), default=func.now())


class Mets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    value = db.Column(db.Numeric)


class Rehydration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    data_collected = db.Column(db.DateTime(timezone=True), default=func.now())


class UserSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    water_goal = db.Column(db.Numeric)
    color_mode = db.Column(db.String(1))
    unit_system = db.Column(db.String(1))
    data_collected = db.Column(db.DateTime(timezone=True), default=func.now())
