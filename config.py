import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    POSTGRES = {
        'user': 'postgres',
        'pw': 'password',
        'db': 'my_database',
        'host': 'localhost',
        'port': '5432',
    }
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:Shubham@localhost:5432/flaskweather'
    SQLALCHEMY_TRACK_MODIFICATIONS = False