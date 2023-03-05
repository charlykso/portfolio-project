#!/usr/bin/python3
"""to check and get the user details"""

from models import storage
from models.user import User
from flask import Flask, jsonify, abort


def get_user(user_id):
    """to get user details"""
    new_list = []
    key = "User." + str(user_id)
    if user_id is None:
        objs = storage.all(User)
        for key, value in objs.items():
            new_list.append(value.to_dict())
    elif key in storage.all(User).keys():
        return jsonify(storage.all(User)[key].to_dict())
    else:
        abort(404)
    return jsonify(new_list)
