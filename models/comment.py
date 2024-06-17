#!/usr/bin/python3
"""
This module defines a class of the Comment model
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Comment(BaseModel, Base):
    """
    Defines Comment class
    """
    __tablename__ = "comments"

    comment_string = Column(String(1028), nullable=False)
    bug_id = Column(String(60), ForeignKey("bugs.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    