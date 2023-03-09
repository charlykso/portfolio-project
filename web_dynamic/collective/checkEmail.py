#!/usr/bin/python3
"""check if the email exists in the db"""

from models import storage
from models.user import User


class CheckEmail:
    """a class to check if email exists"""

    def emailExists(email):
        """a method to check if email exists"""
        key = "User." +email
        # users = storage.all(User)
        for key, value in storage.all(User).items():
            if value.email == email:
                return True
        return False
