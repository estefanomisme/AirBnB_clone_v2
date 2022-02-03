#!/usr/bin/python3
"""11. HBNB filters"""


from flask import Flask, render_template
from models import storage
from markupsafe import escape
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(exception):
    """closes the current session"""
    storage.close()


@app.route("/states")
@app.route("/states_list")
def states_list():
    """Shows a page with all State objects"""
    return render_template("7-states_list.html", states=storage.all('State'))


@app.route("/cities_by_states")
def cities_by_states():
    """Shows a page with all Cities ordered by State"""
    return render_template("8-cities_by_states.html",
                           states=storage.all('State'))


@app.route("/states/<id>")
def states(id):
    """Shows a page with all State objects"""
    state = None
    id = escape(str(id))
    for obj in storage.all("State").values():
        if obj.id == id:
            state = obj
    return render_template("9-states.html", state=state)


@app.route("/hbnb_filters")
def hbnb_filters():
    """Shows a styled page showing all cities, states and amenities"""
    return render_template("10-hbnb_filters.html",
                           states=storage.all('State'),
                           amenities=storage.all('Amenity'))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
