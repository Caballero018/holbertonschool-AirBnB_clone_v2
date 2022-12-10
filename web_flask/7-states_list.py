#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_db(self):
    storage.close()

@app.route('/states_list', strict_slashes=False)
def state_list():
    states = storage.all(State)
    return render_template('7-states_list.py', states = states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
