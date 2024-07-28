#!/usr/bin/python3
"""A script that starts a Flask web application """


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return f"Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return f"HBNB!"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
