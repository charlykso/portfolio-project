#!/usr/bin/python3
"""for the property images"""

from models import storage
from models.property_img import Property_img
from models.property import Property
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route("/properties/<property_id>/images/", methods=['GET'],
                 strict_slashes=False)
def get_images_for_a_property(property_id=None):
    """
    get all images for a property
    """
    new_list = []
    property = storage.get(Property, property_id)
    if property is None:
        abort(404)
    for image in property.property_imgs:
        new_list.append(image.to_dict())
    return jsonify(new_list)


@app_views.route("/images", methods=['GET'],
                 strict_slashes=False)
@app_views.route("/images/<image_id>", methods=['GET'],
                 strict_slashes=False)
def get_all_images(image_id=None):
    """
    get all images
    or get any image with the propertyImg_id that is passed
    """
    new_list = []
    key = "Property_img." + str(image_id)
    if image_id is None:
        objs = storage.all(Property_img)
        for key, value in objs.items():
            new_list.append(value.to_dict())
    elif key in storage.all(Property_img).keys():
        return jsonify(storage.all(Property_img)[key].to_dict())
    else:
        abort(404)
    return jsonify(new_list)


@app_views.route("/images/<image_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_image(image_id=None):
    """
    delete any image by passing the propertyImg_id
    """
    image = storage.get(Property_img, image_id)
    if image is None:
        abort(404)
    image.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/properties/<property_id>/image", methods=['POST'],
                 strict_slashes=False)
def create_image(property_id=None):
    """
    create a new image for a property
    by passing the property id
    """
    if storage.get(Property, request.get_json()["property_id"]) is None:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if "img_path" not in request.get_json():
        abort(400, "Missing image")
    image = Property_img(**request.get_json())
    image.property_id = property_id
    image.save()
    return jsonify(image.to_dict()), 201


@app_views.route("/images/<image_id>", methods=['PUT'],
                 strict_slashes=False)
def update_images(image_id=None):
    """
    update any image by passing the property_img id
    """
    image = storage.get(Property_img, image_id)
    if image is None:
        abort(404)
    key = "Property_img." + str(image_id)
    if key not in storage.all(Property_img).keys():
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    for key, value in request.get_json().items():
        if key not in ["id", "created_at", "updated_at", "property_id"]:
            setattr(image, key, value)
    image.save()
    return jsonify(image.to_dict()), 200
