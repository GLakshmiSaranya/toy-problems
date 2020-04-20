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
    return "Welcome to Project1"

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
        print("connecting to DB")
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
    isuser = db.query(User).get(email)
    
    if (isuser != None):
        if isuser.password == password :
            session["email"] = email
            print("Session created")
            return render_template("login.html", user = email)
        else:
            return render_template("registration.html", msg = "Invalid password")
    else:
        return render_template("registration.html", msg = "Invalid email")

@app.route("/logout", methods = ["GET"])
def logout():
    if "email" in session:  
        session.clear()
        print("session removed")
        return redirect("/register")  
    else:  
        return render_template("msg.html", msg = "User already logged out")  
