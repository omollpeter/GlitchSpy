#!/usr/bin/python3
"""
This module contains class definition for Bug Model
"""


from models.base_model import BaseModel, Base
from models.comment import Comment
from sqlalchemy import Column, String, Integer
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
    status = Column(String(20), default="public", nullable=False)
    upvotes = Column(Integer, default=0, nullable=False)
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

    def comments(self):
        """
        Retrieves all the comments for a specific bug
        """
        from models import storage

        comment_list = []
        for comment in storage.all(Comment).values():
            if comment.bug_id == self.id:
                comment_list.append(comment)

        return comment_list
