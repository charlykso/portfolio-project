#!/usr/bin/python
""" holds class Property_img"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Property_img(BaseModel, Base):
    """Representation of Property_img """
    __tablename__ = 'property_imgs'
    img_path = Column(String(255), nullable=False)
    property_id = Column(String(60), ForeignKey('properties.id'), nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes property_img"""
        super().__init__(*args, **kwargs)