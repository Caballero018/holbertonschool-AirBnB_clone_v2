#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    return "HBNB"


@app.route('/c/<text>')
def text(text):
    return "C {:s}".format(escape(text).replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def text_2(text):
    return "Python {:s}".format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(escape(n))


@app.route('/number_template/<int:n>')
def numb(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_odd(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
