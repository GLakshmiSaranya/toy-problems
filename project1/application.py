import os
import datetime

from flask import Flask, session, render_template, request, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import User, db

app = Flask(__name__)

FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format = FORMAT, level = logging.INFO)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

db.init_app(app)
Session(app)

@app.route("/")
def index():
    if session.get("email") is None:
        return render_template("registration.html", msg = "Please Login here")
    retun "Welcome to my website"

@app.route("/register", methods = ["GET", "POST"])
def register():
    if (request.method == "POST"):
        name = request.form.get("name")
        email = request.form.get("email")
        pwd = request.form.get("pwd")
        datetime = datetime.datetime.now()

        try:
            user = User(name = name, email = email, pwd = pwd, created = datetime)
            db.session.add(user)
	    db.session.commit()
	    return "You have registered sucessfully, Please Login."
	except:
            return "Registration failed..."
        return render_template("registration.html")

@app.route("/onsubmit", methods = ["POST"])
def onsubmit():
    name = request.form.get("name")
    email = request.form.get("email")
    pwd = request.form.get("pwd")
    time = datetime.datetime.now()
    print("Name: " + name + ", email: " + email)       

@app.route("/admin", methods = ["GET"])
def admin():
    users = User.query.order_by(User.created.desc()).all()
    return render_template("adminpage.html", users = users)

@app.route("/authorized", methos = ["POST"])
def authorized():
    email = request.form.get("email")
    pwd = request.form.get("pwd")

    isuser = User.query.filter_by(email = email)
    if (isuser[0].email == email and isuser[0].pwd == pwd):
        session["

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/register")
