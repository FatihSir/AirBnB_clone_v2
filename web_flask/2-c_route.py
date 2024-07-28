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
    display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    text = escape(text.replace("_", " "))
    return f'C {text}'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
