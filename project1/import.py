import os, csv
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def main():
    db.create_all()
    with open("books.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)

        for r in reader:
            new = Book(r[0], r[1], r[2], int(r[3]))
            db.session.add(new)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()