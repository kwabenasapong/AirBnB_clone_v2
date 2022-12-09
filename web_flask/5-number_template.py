#!/usr/bin/python3
""" start a Flask Web application
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Print Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def only_hbnb():
    """ Print HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cissome(text):
    """ Print C + <name> without underscore """
    return("C {}".format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def pythonalone():
    """ Print Python is cool ...by default """
    return("Python is cool")


@app.route('/python/<text>', strict_slashes=False)
def pythonissome(text):
    """ Print Python + <name> without underscore """
    return("Python {}".format(text.replace("_", " ")))


@app.route('/number/<nummer>', strict_slashes=False)
def numberisint(nummer):
    """ Print number if it s a number """
    if nummer.isdigit():
        return("{} is a number".format(nummer))


@app.route('/number_template/<nummer>', strict_slashes=False)
def number_template(nummer):
    """ Print a template with a variable """
    if nummer.isdigit():
        return render_template('5-number.html', name=nummer)
    else:
        return render_template('no_found.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
