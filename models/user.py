#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(200), nullable=False)
    firstname = Column(String(128), nullable=True)
    lastname = Column(String(128), nullable=True)
    gender = Column(String(10), nullable=False)
    phone_no = Column(String(20), nullable=False)
    properties = relationship("Property",
                              backref="user",
                              cascade="all, delete, delete-orphan")
    addresses = relationship("Address",
                             backref="user",
                             cascade="all, delete, delete-orphan")


    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

    @property
    def properties(self):
        """getter attribute returns the list of Property instances"""
        from models.property import Property
        property_list = []
        all_properties = models.storage.all(Property)
        for property in all_properties.values():
            if property.user_id == self.id:
                property_list.append(property)
        return property_list

    @property
    def addresses(self):
        """getter attribute returns the list of Address instances"""
        from models.address import Address
        address_list = []
        all_addresses = models.storage.all(Address)
        for address in all_addresses.values():
            if address.user_id == self.id:
                address_list.append(address)
        return address_list
