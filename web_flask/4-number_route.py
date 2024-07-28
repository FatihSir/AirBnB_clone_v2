#!/usr/bin/python3
"""A script that starts a Flask web application """


from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns Hello HBNB in text format"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """Returns HBNB in text format"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=True)
def cisfun(text):
    """
    Display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    text = escape(text.replace("_", " "))
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=True)
def python(text="is cool"):
    """
     Display “Python ”, followed by the value of the text variable
     (replace underscore _ symbols with a space )
     """
    text = escape(text.replace("_", " "))
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display “n is a number” only if n is an integer"""
    return f'{escape(n)} is a number'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
