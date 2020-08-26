from flask import Flask, request, render_template, redirect
import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import psycopg2

app = Flask(__name__)

# DATABASE_URL=os.system("heroku config:get DATABASE_URL -a flasktest00")
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
                                        "postgresql://postgres:assa1221@localhost:5432/names_years"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# migrate.init_app(app, db)

class NY(db.Model):
    name = db.Column(db.String(),primary_key=True)
    year = db.Column(db.Integer)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __repr__(self):
        return '<User {}>'.format(self.name)

db.create_all()
db.session.commit()


@app.route('/', methods=('GET','POST'))
def index():
    if request.method == 'GET':
        datas = NY.query.all()


        results = [
            {
                "name": dat.name,
                "year": dat.year
            } for dat in datas]

        return render_template("index.html", dbinfo = results)

    if request.method == 'POST':
        if request.form.get('name') is not None:
            newname = request.form.get('name')
        if request.form.get('year') is not None:
            newyear = request.form.get('year')

        new_in_db = NY(name=newname,year=newyear)
        db.session.add(new_in_db)
        db.session.commit()


        return redirect("/")


# @app.route('/')
# def hello():
#     return {"hello": "world"}


if __name__ == '__main__':
    app.run(debug=True)