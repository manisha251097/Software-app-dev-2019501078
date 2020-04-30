import os
import datetime
from flask import Flask, session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
import csv
from  models import *
from create import app

app = Flask(__name__)
os.environ['DATABASE_URL'] =  'postgres://vzntuvxhqpksbv:caf5aeb37d4471b25d9dbe66de5d8a4168daacee830458b9a73639e2f43e6eb4@ec2-54-210-128-153.compute-1.amazonaws.com:5432/dbo5a5cl9hl2qc'
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
# Session = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    print(session.get('email'))
    if session.get('email') is None:
        return render_template("index.html")
    return render_template("thanks.html")
    

@app.route("/" , methods=["GET","post"])
def register():
    if request.method == "GET":
        return "PLEASE SUBMIT THE FORM"
    else:
        name = request.form.get("name")
        email=request.form.get("mail")
        password=request.form.get("passw")
        u = user(username=name,email=email,password=password)
        # session = Session()
        p = user.query.get(email)
        if p is None:
            db.add(u)
            db.commit()
            return render_template("index.html", status="success",name=name)
        else :
            return render_template("index.html",name="Already registered")
@app.route("/login",methods=["GET","POST"])
def login():
        return render_template("login.html")
@app.route("/login/" ,methods=["GET","POST"])
def thanks():
    if request.method == "GET":
        # return render_template("thanks.html")
        return "Please enter credentials in home page"
    else:
        email=request.form.get("mail")
        password=request.form.get("passw")
        e = user.query.get(email)
        if e is None :
            print(e)
            return render_template("login.html", message="invalid credentails")
        u = user.query.filter_by(email=email).first()

        if u.password != password:
            return render_template("login.html", message="invalid pass")
        else:
            name=u.username
            session['email'] = u.email
            return render_template("thanks.html", name=name)
@app.route("/search",methods=["GET","POST"])
def search():
    try:
        inp = str(request.form.get("search"))
        print("input is"+inp)
        with open('books.csv', newline= "") as file:
            readData = [row for row in csv.DictReader(file)]
            for i in range(len(readData)):
                if readData[i]['title'] == inp:
                    return render_template("bookPage.html", isbn=readData[i]['isbn']
                    )
            return "Book not found"
    except:
        return sys.exc_info()[0]

@app.route("/bookPage/<string:isbn>", methods=["GET", "POST"])
def bookpage(isbn) :

    if request.method == "GET" :
        if session.get("email") :
            return render_template("bookPage.html", isbn=isbn)
        else :
            redirect(url_for("login"))
    else :
        if session.get("email") :
            return isbn
        else :
            redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.clear()
    return render_template("login.html")