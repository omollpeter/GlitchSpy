#!/usr/bin/python3
"""
This module defines a class of the Comment model
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class Comment(BaseModel, Base):
    """
    Defines Comment class
    """
    __tablename__ = "comments"

    comment_string = Column(String(1028), nullable=False)
    bug_id = Column(String(60), ForeignKey("bugs.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes Comment instance
        """
        super().__init__(*args, **kwargs)
