#!/usr/bin/python3
"""This is for the buy page"""

import uuid
# import models.property_img
from models import storage
from models.user import User
# from models.property import Property
# from models.property_img import Property_img
# from models.address import Address
# from os import environ
from flask import Flask, render_template
# from api.v1.app import close_db

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """Remove the current sqlalchemy session"""
    storage.close()


@app.route("/", strict_slashes=False)
def index():
    """landing page"""
    return render_template("index.html", cache_id=uuid.uuid4)

@app.route("/properties", strict_slashes=False)
def property():
    """List all the users"""
    return render_template("testbase.html",
                           cache_id=uuid.uuid4())

@app.route("/buy", strict_slashes=False)
def user():
    """List of all users"""
    users = storage.all(User).values()
    users = sorted(users, key=lambda k: k.firstname)

    return render_template("buy.html",
                           users=users,
                           cache_id=uuid.uuid4())

@app.route("/details/<property_id>", strict_slashes=False)
def single_property(property_id):
    """Get the details of one property"""
    return render_template("details.html", cache_id=uuid.uuid4)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5002, debug=True)
    