#!/usr/bin/python
""" holds class Property"""
import models
from models.base_model import BaseModel, Base
import models.property_img
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Property(BaseModel, Base):
    """Representation of property """
    __tablename__ = 'properties'
    gen_property_id = Column(String(60), nullable=False)
    status = Column(String(20), nullable=False)
    description = Column(String(255), nullable=False)
    state = Column(String(128), nullable=False)
    availability = Column(String(20), nullable=False)
    landmark = Column(String(200), nullable=True)
    search_term = Column(String(255), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    type = Column(String(60), nullable=False)
    price = Column(Integer, nullable=False)
    property_imgs = relationship("Property_img",
                              backref="property",
                              cascade="all, delete, delete-orphan")
    reviews = relationship("Review",
                              backref="property",
                              cascade="all, delete, delete-orphan")


    def __init__(self, *args, **kwargs):
        """initializes property"""
        super().__init__(*args, **kwargs)

    @property
    def property_imgs(self):
        """getter attribute returns the list of Property_img instances"""
        from models.property_img import Property_img
        property_img_list = []
        all_property_imgs = models.storage.all(Property_img)
        for img in all_property_imgs.values():
            if img.property_id == self.id:
                property_img_list.append(img)
        return property_img_list

    @property
    def reviews(self):
        """getter attribute returns the list of Review instances"""
        from models.review import Review
        review_list = []
        all_reviews = models.storage.all(Review)
        for review in all_reviews.values():
            if review.property_id == self.id:
                review_list.append(review)
        return review_list
