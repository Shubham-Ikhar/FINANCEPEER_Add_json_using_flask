from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class JsonData(UserMixin, db.Model):
    userId = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    title = db.Column(db.String(1000), unique=True)
    body = db.Column(db.String(10000), unique=True)
