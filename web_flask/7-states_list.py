#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape
import sys
sys.path.append("..")
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_db(self):
    storage.close()

@app.route('/states_list')
def state_list():
    stat= storage.all(State)
    s = []
    for s in stat:
        s.append(stat)
    return render_template('7-states_list.py', states=s)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
