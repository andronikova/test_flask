from flask import Flask, request, render_template, redirect
import sqlite3 as sql
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# db = SQLAlchemy()
# migrate = Migrate()

app = Flask(__name__)

DATABASE = 'test.db'

# app.config.from_mapping(
#     SECRET_KEY=os.environ.get('SECRET_KEY') or 'dev_key',
#     SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
#                             'sqlite:///' + os.path.join(app.instance_path, 'task_list.sqlite'),
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
# )

# print(os.environ.get('DATABASE_URL'))
#
# db.init_app(app)
# migrate.init_app(app, db)

@app.route('/', methods=('GET','POST'))
def index():
    if request.method == 'GET':
        with sql.connect(DATABASE) as con:
                con.row_factory = sql.Row
                cur = con.cursor()

                cur.execute("SELECT * FROM names")
                rows = cur.fetchall()

                dict = {}
                for row in rows:
                    dict[row['name']] = row['year']

        con.close()

        return render_template("index.html", dbinfo = dict)

    if request.method == 'POST':
        if request.form.get('name') is not None:
            name = request.form.get('name')
        if request.form.get('year') is not None:
            year = request.form.get('year')

        with sql.connect(DATABASE) as con:
                con.row_factory = sql.Row
                cur = con.cursor()

                # cur.execute("CREATE TABLE 'names' ('year' INTEGER NOT NULL, 'name' VARCHAR(255) NOT NULL)")
                cur.execute("INSERT INTO names (name, year) VALUES (:name,:year)", {'name':name, "year": year})
        con.close()

        return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)