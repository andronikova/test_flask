from flask import Flask, request, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'dev_key',
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
                            'sqlite:///' + os.path.join(app.instance_path, 'task_list.sqlite'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

print(os.environ.get('DATABASE_URL'))

db.init_app(app)
migrate.init_app(app, db)

@app.route('/', methods=('GET','POST'))
def index():
    if request.method == 'GET':
        dbinfo = {}
        return render_template("index.html", dbinfo=dbinfo)

    if request.method == 'POST':
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.Text(), nullable=False)


    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)