#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape
import sys
sys.path.append("..")
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def state_list():
    """Returns a HTML with states list"""
    state_dict = storage.all(State)
    city_dict = storage.all(City)
    states_list = []
    for state in state_dict.values():
        states_list.append(state)
    return render_template('8-cities_by_states.html', states=state_list, cities=city_dict)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
