#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape
from ..models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_db():
    storage.close()

@app.route('/')
def list():
    return render_template('7-states_list.py')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
