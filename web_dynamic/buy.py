#!/usr/bin/python3
"""This is for the buy page"""

# import models.property_img
# import uuid
# from models import storage
# from models.user import User
# from models.property import Property
# from models.property_img import Property_img
# from models.address import Address
# from os import environ
from flask import Flask, render_template
# from api.v1.app import close_db

app = Flask(__name__)

# @app.teardown_appcontext
# def close_db(error):
#     """Remove the current sqlalchemy session"""
#     storage.close()


@app.route("/properties", strict_slashes=False)
def property():
    """List all the users"""
    return render_template("testbase.html")


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5002, debug=True)
    