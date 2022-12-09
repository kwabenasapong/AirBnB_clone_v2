#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base, os_type_storage
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """

    if os_type_storage == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
#        place_amenities = relationship("Place",
#                                       secondary=place_amenity,
#                                       backref="amenities")
    else:
        name = ""
