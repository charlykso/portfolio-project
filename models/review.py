#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer


class Review(BaseModel, Base):
    """Representation of Review """
    __tablename__ = 'reviews'
    rate = Column(Integer, nullable=False)
    property_id = Column(String(60), ForeignKey('properties.id'), nullable=False)
    text = Column(String(1024), nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)