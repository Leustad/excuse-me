import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)

import excuse_me.views.main
