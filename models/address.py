#!/usr/bin/python
""" holds class Address"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Address(BaseModel, Base):
    """Representation of Address """
    __tablename__ = 'addresses'
    country = Column(String(128), nullable=False)
    state = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    street = Column(String(128), nullable=False)
    landmark = Column(String(128), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes Address"""
        super().__init__(*args, **kwargs)
