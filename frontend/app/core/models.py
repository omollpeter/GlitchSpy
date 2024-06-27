#!/usr/bin/python3
"""
This module contains all the models for the core functionality
"""


from frontend.app import db
from datetime import datetime, timezone
import uuid


class Bug(db.Model):
    """
    Defines a Bug class which is a report for a bug
    """
    __tablename__ = "bugs"

    id = db.Column(db.String(60), primary_key=True, default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(1028), nullable=True)
    category = db.Column(db.String(60), nullable=False)
    severity = db.Column(db.String(60), nullable=False)
    product = db.Column(db.String(60), nullable=False)
    attachment = db.Column(db.String(1028), nullable=True)
    reportedBy = db.Column(db.String(60), default="anonymous")
    status = db.Column(db.String(20), default="public", nullable=False)
    upvotes = db.Column(db.Integer, default=0, nullable=False)
    comments = db.relationship(
        "Comment",
        backref="bug",
        cascade="all, delete, delete-orphan"
    )

    def __init__(self, name, category, severity, product, upvotes=0, attachment="", description="", reportedBy="anonymous", status="public"):
        """
        Initializes Bug instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at
        self.name = name
        self.category = category
        self.severity = severity
        self.product = product
        self.upvotes = upvotes
        self.attachment = attachment
        self.description = description
        self.reportedBy = reportedBy
        self.status = status

    def __repr__(self):
        """Returns the official string representation"""
        return f"<Bug {self.name}>"


class Comment(db.Model):
    """
    Defines Comment class
    """
    __tablename__ = "comments"

    id = db.Column(db.String(60), primary_key=True, default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    comment_string = db.Column(db.String(1028), nullable=False)
    bug_id = db.Column(db.String(60), db.ForeignKey("bugs.id"), nullable=False)

    def __init__(self, comment_string):
        """
        Initializes Comment instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at
        self.comment_string = comment_string
