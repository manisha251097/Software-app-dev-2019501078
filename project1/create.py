import os

from flask import Flask, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

# Import table definitions.
from models import *

app = Flask(__name__)

# Tell Flask what SQLAlchemy databas to use.

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://vzntuvxhqpksbv:caf5aeb37d4471b25d9dbe66de5d8a4168daacee830458b9a73639e2f43e6eb4@ec2-54-210-128-153.compute-1.amazonaws.com:5432/dbo5a5cl9hl2qc'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)

def main():
    # Create tables based on each table definition in `models`
    db.create_all()

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context():
        main()