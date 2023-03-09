#!/usr/bin/python3
"""Object that handles the address route for the api"""
from models.address import Address
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, request


@app_views.route("/users/<user_id>/addresses", methods=['GET'],
                 strict_slashes=False)
def get_address_for_a_user(user_id=None):
    """
    get a address that is associated to a user
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    new_list = []
    for address in user.addresses:
        new_list.append(address.to_dict())
    return jsonify(new_list)


@app_views.route("/addresses", methods=['GET'],
                 strict_slashes=False)
@app_views.route("/addresses/<address_id>", methods=['GET'],
                 strict_slashes=False)
def get_all_addresses(address_id=None):
    """
    get all addresses
    or get any address with the address_id that is passed
    """
    new_list = []
    key = "Address." + str(address_id)
    if address_id is None:
        objs = storage.all(Address)
        for key, value in objs.items():
            new_list.append(value.to_dict())
    elif key in storage.all(Address).keys():
        return jsonify(storage.all(Address)[key].to_dict())
    else:
        abort(404)
    return jsonify(new_list)


@app_views.route("/addresses/<address_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_address(address_id=None):
    """
    delete any address that the address_id is passed
    """
    address = storage.get(Address, address_id)
    if address is None:
        abort(404)
    address.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/users/<user_id>/addresses", methods=['POST'],
                 strict_slashes=False)
def create_address(user_id=None):
    """
    create a new address for a user
    by passing th user id
    """
    if storage.get(User, user_id) is None:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if "country" not in request.get_json():
        abort(400, "Missing country")
    if "state" not in request.get_json():
        abort(400, "Missing state")
    if "street" not in request.get_json():
        abort(400, "Missing street")
    if "city" not in request.get_json():
        abort(400, "Missing city")
    if "landmark" not in request.get_json():
        abort(400, "Missing landmark")
    if "user_id" not in request.get_json():
        abort(400, "Missing user_id")
    if storage.get(User, request.get_json()["user_id"]) is None:
        abort(404)
    address = Address(**request.get_json())
    address.user_id = user_id
    address.save()
    return jsonify(address.to_dict()), 201


@app_views.route("/addresses/<address_id>", methods=['PUT'],
                 strict_slashes=False)
def update_address(address_id=None):
    """
    update any users address by passing the address id
    """
    address = storage.get(Address, address_id)
    if address is None:
        abort(404)
    key = "Address." + str(address_id)
    if key not in storage.all(Address).keys():
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    for key, value in request.get_json().items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(address, key, value)
    address.save()
    return jsonify(address.to_dict()), 200
