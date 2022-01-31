#!/usr/bin/python3
"""2. C is fun!"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """displays a text in '/'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """displays a text in '/hbnb'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    """displays a text in '/c/<text>' depending on text"""
    return f"C {escape(text).replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
