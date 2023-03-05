#!/usr/bin/python3
"""index file"""

from api.v1.views import app_views
from models import storage
from models.base_model import BaseModel, Base
from models.address import Address
from models.property import Property
from models.review import Review
from models.property_img import Property_img
from models.user import User
from flask import jsonify

classes = {
           "addresses": Address,
           "properties": Property,
           "reviews": Review,
           "property_imgs": Property_img,
           "users": User,
           }


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """API status"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def obj_count():
    """retrieve number of objects by type"""
    obj_count = {}
    for key, value in classes.items():
        obj_count[key] = storage.count(value)
    return jsonify(obj_count)


if __name__ == '__main__':
    pass
