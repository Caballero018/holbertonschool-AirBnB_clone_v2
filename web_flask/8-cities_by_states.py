#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(execute):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def state_list():
    """Returns a HTML with states list"""
    state_dict = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=state_dict)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
