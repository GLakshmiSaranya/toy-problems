import os
from dbtable import *
import datetime

from flask import Flask, session, render_template, request, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

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
#session = db()

@app.route("/")
def index():
    return "Welcome"

@app.route("/register", methods = ["GET", "POST"])
def register():
    if (request.method == "POST"):
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("pwd")
        created = datetime.datetime.now()
        print("Name: ", name)
        print("Email: ", email)
        print("Time: ", created)
        user = User(name = name, email = email, password = password, created = created)
        try:
            session.add(user)
            print("Add new user")
            session.commit()
            print("Add commit")
            return render_template("msg.html", msg = "Your registration is successfully completed")
        except:
            return render_template("msg.html", msg = "Your registration failed... Please try again")
    return render_template("registration.html")     

@app.route("/admin", methods = ["GET"])
def admin():
    users = db.query(User)
    return render_template("adminpage.html", users = users)

@app.route("/authorized", methods = ["POST"])
def authorized():
    email = request.form.get("email")
    password = request.form.get("pwd")

    isuser = db.query(User).filter_by(email = email)
    if (isuser[0].email == email and isuser[0].password == password):
        session["email"] = email
        print("session created")
        return render_template("msg.html", msg = "Successfully logged in")
    return render_template("register.html", text = "Invalid email or password")

@app.route("/logout")
def logout():
    if "email" in session:  
        session.clear()
        print("session removed")
        return redirect("/register")  
    else:  
        return render_template("msg.html", msg = "User already logged out")  
