#!/usr/bin/python3
"""8. List of states"""

from flask import Flask, render_template
from models import storage
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False
states = storage.all('State')


@app.teardown_appcontext
def close(exception):
    """closes the current session"""
    storage.close()


@app.route("/states_list")
def states_list():
    """Shows a page with all State objects"""
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
