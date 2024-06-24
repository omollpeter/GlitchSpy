#!/usr/bin/python3
"""
This module defines a class all models for the accounts
"""


from app import db
from datetime import datetime, timezone
import uuid
from hashlib import md5
from flask_login import UserMixin # To allow user implement is_authenticated, is_active, is_anonymous, get_id()


class User(UserMixin, db.Model):
    """
    Defines a user class
    """
    __tablename__ = "users"

    id = db.Column(db.String(60), primary_key=True, default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    contact = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, first_name, last_name, email, password, contact, is_admin=False):
        """
        Initializes the instance attributes a User instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = md5(password.encode()).hexdigest()
        self.contact = contact
        self.is_admin = is_admin

    def __repr__(self):
        """
        Returns the current users email
        """
        return f"<User {self.email}>"


class Organization(db.Model):
    """
    Defines a organization class
    """
    __tablename__ = "organizations"

    id = db.Column(db.String(60), primary_key=True, default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)

    def __init__(self, name, email, password):
        """
        Initializes the instance attributes a User instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at
        self.name = name
        self.email = email
        self.password = md5(password.encode()).hexdigest()

    def __repr__(self):
        """
        Returns the current organization email
        """
        return f"<Organization {self.email}>"
