#!/usr/bin/python3
"""
Module that starts Flask
"""
from flask import Flask, render_template
from models import storage
app = flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML states page listed A-Z"""
    states_all = sorted(list(storage.all(State).values()))
    return (render_templates('7-states_list.html', states_all=states_all))


@app.teardown_appcontext
def teardown():
    """After request removes current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
