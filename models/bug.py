#!/usr/bin/python3
"""
This module contains class definition for Bug Model
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Bug(BaseModel, Base):
    """
    Defines a Bug class which is a report for a bug
    """
    __tablename__ = "bugs"

    name = Column(String(60), nullable=False)
    description = Column(String(1028), nullable=True)
    category = Column(String(60), nullable=False)
    severity = Column(String(60), nullable=False)
    product = Column(String(60), nullable=False)
    attachment = Column(String(1028), nullable=True)
    reportedBy = Column(String(60), default="anonymous")
    comments = relationship(
        "Comment",
        backref="bug",
        cascade="all, delete, delete-orphan"
    )

    def __init__(self, *args, **kwargs):
        """
        Initializes Bug instance
        """
        super().__init__(*args, **kwargs)
