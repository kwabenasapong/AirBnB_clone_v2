#!/usr/bin/python3
""" start a Flask Web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ render states """
    list_state = storage.all(State).values()
    print(list_state)
    return render_template('7-states_list.html', list_state=list_state)


@app.teardown_appcontext
def teardown_db(exit):
    """ Close storage """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
