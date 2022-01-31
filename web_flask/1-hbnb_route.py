#!/usr/bin/python3
"""1. HBNB"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """displays a text in '/'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """displays a text in '/hbnb'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
