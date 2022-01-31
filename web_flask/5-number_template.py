#!/usr/bin/python3
"""5. Number template - starts a Flask web application"""


from flask import Flask, render_template
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


@app.route("/number_template/<int:n>")
def number_template(n):
    """displays a template of a HTML page in '/number_template/<n>'"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
