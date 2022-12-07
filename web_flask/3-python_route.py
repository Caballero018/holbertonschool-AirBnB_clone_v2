#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def Hello_HBNB():
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    return "HBNB"


@app.route('/c/<text>')
def text(text):
    return "C {:s}".format(escape(text).replace('_', ' '))


@app.route('/python/<text>')
def text(text):
    return "Python {:s}".format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
