#!/usr/bin/python3
"""
This module defines a class for User model
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Defines a user class
    """
    __tablename__ = "users"

    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(300), nullable=False)
    contact = Column(String(60), nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes the instance attributes a User instance
        """
        super().__init__(*args, **kwargs)
