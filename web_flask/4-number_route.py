#!/usr/bin/python3
"""4. Is it a number? - starts a Flask web application"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """displays a static text in '/'"""
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    """displays a static text in '/hbnb'"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """displays a text in '/c/<text>'"""
    return "C {}".format(escape(text).replace('_', ' '))


@app.route("/python")
@app.route("/python/<text>")
def python_text(text='is cool'):
    """displays a text in '/python/<text>' with a default value"""
    return "Python {}".format(escape(text).replace('_', ' '))


@app.route("/number/<int:n>")
def number(n):
    """displays a number in '/number/<n>'"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
