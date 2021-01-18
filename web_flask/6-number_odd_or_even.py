#!/usr/bin/python3
"""
Module starts Flask web app
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints "Hello HBNB!" """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ prints "HBNB" """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """displays "C" followed by the value of the text var"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """displays "Python + text var" """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """displays N is a number only if is int"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """displays a HTML page"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/int;,<odd_even>', strict_slashes=False)
def odd_or_even(n):
    """displays html page only if n is int"""
    if n % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
        return render_template('6-number_odd_or_even.html', n=n,
                               odd_even=odd_even')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
