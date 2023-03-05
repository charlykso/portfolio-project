#!/usr/bin/python3
"""Object to access reviews for properties"""

from flask import Flask, abort, request, jsonify
from api.v1.views import app_views
from models import storage
from models.property import Property
from models.review import Review


@app_views.route("/properties/<property_id>/reviews", methods=['GET'],
                 strict_slashes=False)
def get_reviews_for_a_property(property_id=None):
    """
    get all reviews that is associated to a property
    """
    property = storage.get(Property, property_id)
    if property is None:
        abort(404)
    new_list = []
    for review in property.reviews:
        new_list.append(review.to_dict())
    return jsonify(new_list)


@app_views.route("/reviews/<review_id>", methods=['GET'],
                 strict_slashes=False)
def get_review(review_id=None):
    """
    retrieve one review
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route("/reviews/<review_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id=None):
    """
    delete a review that the id was passed
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    review.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/properties/<property_id>/reviews", methods=['POST'],
                 strict_slashes=False)
def create_review(property_id=None):
    """
    create a review for a property
    by using the property_id to select the property
    """
    if storage.get(Property, property_id) is None:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if "property_id" not in request.get_json():
        abort(400, "Missing property_id")
    if storage.get(Property, request.get_json()["property_id"]) is None:
        abort(404)
    if "text" not in request.get_json():
        abort(400, "Missing text")
    if "rate" not in request.get_json():
        abort(400, "Missing rate")

    review = Review(**request.get_json())
    review.property_id = property_id
    review.save()
    return jsonify(review.to_dict()), 201


@app_views.route("/reviews/<review_id>", methods=['PUT'],
                 strict_slashes=False)
def update_review(review_id=None):
    """
    update a review
    by passing the review_id
    """
    key = "Review." + str(review_id)
    if key not in storage.all(Review).keys():
        abort(404)
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    for key, value in request.get_json().items():
        if key not in ["id", "created_at", "update_at",
                       "user_id", "place_id"]:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
