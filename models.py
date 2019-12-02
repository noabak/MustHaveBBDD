import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))  # this connects to a database either on Heroku or on localhost

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True) #user name must be unique
    email = db.Column(db.String, unique=True) #email must be unique
    secret_number = db.Column(db.Integer, unique=False) #must not be unique across user objects
    password= db.Column(db.String)
    session_token = db.Column(db.String)
    deleted= db.Column(db.Boolean, default=False)