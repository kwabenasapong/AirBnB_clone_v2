#!/usr/bin/python3
""" start a Flask Web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.base_model import os_type_storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """ render states """
    if os_type_storage == 'db':
        list_state = storage.all('State').values()
    else:
        list_state = storage.all(State).values()
    return render_template('9-states.html',
                           list_state=list_state, st_id=0)


@app.route('/states/<st_id>', strict_slashes=False)
def states_list_id(st_id):
    """ render states with st_id """
    if os_type_storage == 'db':
        list_state = storage.all('State').values()
    else:
        list_state = storage.all(State).values()
    return render_template('9-states.html',
                           list_state=list_state, st_id=st_id)


@app.teardown_appcontext
def teardown_db(exit):
    """ Close storage """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
