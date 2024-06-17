#!/usr/bin/python3
"""
This module defines a class for Organization model
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Organization(BaseModel, Base):
    """
    Defines a organization class
    """
    name = Column(String(60), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(300), nullable=False)
