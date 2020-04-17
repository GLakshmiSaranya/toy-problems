from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    name = db.Column(db.String(50), index = False, unique = True, nullable = False)
    email = db.Column(db.String(50), index =  True, unique = True, nullable = False)
    password = db.Column(db.String(20))
    created = db.Column(db.DateTime, index = False, unique = False, nullable = False)

    def __init__(self, name, email, password) :
        self.name = name
        self.email = email
        self.password = password
        self.created = datetime.now()

    def __repr__(self):
        return self.email