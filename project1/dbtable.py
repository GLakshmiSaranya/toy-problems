import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)

class User(db.Model):
    __tablename__ = "users"
    name = db.Column(db.String(50), index = False, unique = True, nullable = False)
    email = db.Column(db.String(50), primary_key = True)
    password = db.Column(db.String(20), index = False, unique = False, nullable = False)
    created = db.Column(db.DateTime, index = False, unique = False, nullable = False)

    def _init_(self,name,email,password,timestamp):
        self.name = name
        self.email = email
        self.password = password
        self.timestamp = timestamp
    
    def __repr__(self):
        return self.email

class Book(db.Model):
    __tablename__ = "bookstable"
    isbn = db.Column(db.String, primary_key = True)
    title = db.Column(db.String, unique = False, nullable = False)
    author = db.Column(db.String, unique = False, nullable = False)
    year = db.Column(db.String, unique = False)

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

def main():
    db.create_all()
    
if __name__ == "__main__":
    with app.app_context():
        main()