#!/usr/bin/python3
"""A script that starts a Flask web application """


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return f"Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
