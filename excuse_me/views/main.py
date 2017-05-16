import json
import unicodedata
import random
import os
import sqlite3
from flask import render_template
from excuse_me import app, db


def get_data():
    db_path = os.path.join("excuses.db")
    with sqlite3.connect(db_path) as connection:
        curr = connection.cursor()
        curr.execute('SELECT * FROM excuses_data')
        all_data = curr.fetchall()
        return all_data


@app.route('/', methods=['GET'])
def excuse_main():
    excuse = random.choice(get_data())[1]

    return render_template('main.html', excuse=excuse)


@app.route('/get_excuse', methods=['GET', 'POST'])
def get_excuse():
    excuse = str(random.choice(get_data())[1])
    return excuse
