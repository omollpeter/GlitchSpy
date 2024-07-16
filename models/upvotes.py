#!/usr/bin/python3
"""
This module defines a class of the Upvote model
"""


from models.base_model import Base
from sqlalchemy import Column, String, Integer


class Upvote(Base):
    """
    Defines upvote class
    Stores users who have upvoted a specific bug
    """
    __table_name__ = "upvotes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bug_id = Column(String(60), nullable=False)
    upvoted_by = Column(String(60), nullable=False)
