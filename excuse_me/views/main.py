from flask import render_template
from excuse_me import app


@app.route('/', methods=['GET'])
def excuse_main():
    return 'HELLOO'
