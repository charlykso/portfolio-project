#!/usr/bin/python3
"""to check and get the user details"""

from models import storage
from flask import abort


def get_user(cls, user_id):
    """to get user details"""
    # new_list = []
    key = "User." + str(user_id)
    if user_id is None:
        abort(400, "Missing user id")
    elif key in storage.all(cls).keys():
        return storage.all(cls)[key].to_dict()
    else:
        abort(404)
