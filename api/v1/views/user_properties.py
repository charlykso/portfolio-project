#!/usr/bin/python3
"""Objects for properties """

# import urllib.request, json
import requests, json
from models.user import User
from models.property import Property
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, request
from api.v1.collectives import checkUser


@app_views.route("/users/<user_id>/properties", methods=['GET'],
                 strict_slashes=False)
def get_properties_for_a_user(user_id=None):
    """
    get all properties that is associated to a user
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    new_list = []
    for property in user.properties:
        new_list.append(property.to_dict())
    return jsonify(new_list)


@app_views.route("/properties/<property_id>", methods=['GET'],
                 strict_slashes=False)
@app_views.route('/properties', methods=['GET'],
                 strict_slashes=False)
def get_property(property_id=None):
    """
    retrieve one or all properties
    """
    new_list = []
    key = "Property." + str(property_id)
    if property_id is None:
        objs = storage.all(Property)
        for key, value in objs.items():
            new_list.append(value.to_dict())
    elif key in storage.all(property).keys():
        return jsonify(storage.all(Property)[key].to_dict())
    else:
        abort(404)
    return jsonify(new_list)


@app_views.route("/properties/<property_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_property(property_id=None):
    """
    delete a property that the id was passed
    """
    property = storage.get(Property, property_id)
    if property is None:
        abort(404)
    property.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/users/<user_id>/properties", methods=['POST'],
                 strict_slashes=False)
def create_property(user_id=None):
    """
    create a property for a user
    by using the user_id to select the user
    """
    propertyUrl = "http://0.0.0.0:5004/api/v1/properties/"
    userUrl = "http://127.0.0.1:5004/api/v1/users/"
    if storage.get(User, user_id) is None:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if "user_id" not in request.get_json():
        abort(400, "Missing user_id")
    if storage.get(User, request.get_json()["user_id"]) is None:
        abort(404)
    if "state" not in request.get_json():
        abort(400, "Missing state")
    if "status" not in request.get_json():
        abort(400, "Missing status")
    if "description" not in request.get_json():
        abort(400, "Missing description")
    if "availability" not in request.get_json():
        abort(400, "Missing availability")
    if "landmark" not in request.get_json():
        abort(400, "Missing landmark")
    if "type" not in request.get_json():
        abort(400, "Missing type")
    if "gen_property_id" not in request.get_json():
        abort(400, "Missing the property id from the general property db")
    search_term = request.get_json()['state'].upper()
    +" "+ request.get_json()['landmark'].upper()
    +" "+ request.get_json()['status'].upper()
    +" "+ request.get_json()['state'].upper()
    +" "+ request.get_json()['type'].upper()

    propertyRes = requests.get(
        propertyUrl + request.get_json()['gen_property_id'])
    propertyData = propertyRes.json()

    userRes = requests.get(
        userUrl + propertyData['user_id']
    )
    userData = userRes.json()

    userInfo = checkUser(userData['user_id'])
    
    if userInfo['firstname'].lower() == \
        request.get_json()['firstname'].lower() and \
        userInfo['lastname'].lower() == \
            request.get_json()['lastname'].lower():
      property = Property(**request.get_json())
      property.search_term = search_term
      property.user_id = user_id
      property.save()

      return jsonify(property.to_dict()), 201
  
    abort(400, "Property didn't match the owner!")


@app_views.route("/property/<property_id>", methods=['PUT'],
                 strict_slashes=False)
def update_property(property_id=None):
    """
    update a property
    by passing the property_id
    """
    key = "Property." + str(property_id)
    if key not in storage.all(Property).keys():
        abort(404)
    property = storage.get(Property, property_id)
    if property is None:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    for key, value in request.get_json().items():
        if key not in ["id", "created_at", "updated_at",
                       "user_id", "gen_property_id"]:
            setattr(property, key, value)
    property.save()
    return jsonify(property.to_dict()), 200
