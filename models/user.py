#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base, os_type_storage
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """

    if os_type_storage == "db":
        __tablename__ = "users"
        email = Column(String(128),  nullable=False)
        password = Column(String(128),  nullable=False)
        first_name = Column(String(128),  nullable=True)
        last_name = Column(String(128),  nullable=True)
        places = relationship('Place', cascade="all, delete", backref='user')
        reviews = relationship('Review', cascade="all, delete", backref='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
