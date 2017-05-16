import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'excuse_me.db'
CSRF_ENABLED = True
SECRET_KEY = os.urandom(24)
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

# define the full path for the db
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the db uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
