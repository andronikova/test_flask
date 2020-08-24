import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    POSTGRES = {
        'user': 'postgres',
        'pw': 'password',
        'db': 'my_database',
        'host': 'localhost',
        'port': '5432',
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
    %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/mydb'
        # os.environ.get('DATABASE_URL') or \
        # 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False