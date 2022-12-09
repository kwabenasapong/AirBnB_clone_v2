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


@app.route('/hbnb_filter', strict_slashes=False)
def hbnb_filter():
    """ render hbnbn filters """
    if os_type_storage == 'db':
        l_state = storage.all('State').values()
        l_city = storage.all('City').values()
        l_amenity = storage.all('Amenity').values()
    else:
        l_state = storage.all(State).values()
        l_city = storage.all(City).values()
        l_amenity = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           l_state=l_state, l_city=l_city,
                           l_amenity=l_amenity)


@app.route('/hbnb', strict_slashes=False)
def hbnb_all():
    """ render hbnbn places """
    if os_type_storage == 'db':
        l_state = storage.all('State').values()
        l_place = storage.all('Place').values()
        l_amenity = storage.all('Amenity').values()
    else:
        l_state = storage.all(State).values()
        l_place = storage.all(Place).values()
        l_amenity = storage.all(Amenity).values()
    return render_template('100-hbnb.html',
                           l_state=l_state, l_place=l_place,
                           l_amenity=l_amenity)


@app.teardown_appcontext
def teardown_db(exit):
    """ Close storage """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
