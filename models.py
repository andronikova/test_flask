from flask_sqlalchemy import SQLAlchemy
# from app import db


db = SQLAlchemy()


class NY(db.Model):
    name = db.Column(db.String(),primary_key=True)
    year = db.Column(db.Integer)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __repr__(self):
        return '<User {}>'.format(self.name)

