#!/usr/bin/python3
"""
This module contains class definition for the base model - BaseModel
All data models created for this app will inherit from the BaseModel
"""


from datetime import datetime, timezone
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from hashlib import md5


# Define a time format string
time_frmt = "%Y-%m-%dT%H:%M:%S.%f"

# Define a declarative_base class to map our models to a database table
Base = declarative_base()


class BaseModel:
    """
    Defines a base model class. All models subclasses of this class
    """
    id = Column(String(60), primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))

    def __init__(self, *args, **kwargs):
        """
        Initializes the instance attributes a BaseModel instance
        """
        if kwargs:
            if kwargs.get("password"):
                kwargs["password"] = md5(
                    kwargs["password"].encode()
                ).hexdigest()
            for key, value in kwargs.items():
                setattr(self, key, value)
            if kwargs.get("created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                    kwargs["created_at"], time_frmt
                )
            else:
                self.created_at = datetime.now(timezone.utc)

            if kwargs.get("updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], time_frmt
                )
            else:
                self.updated_at = datetime.now(timezone.utc)

            if not kwargs.get("id"):
                self.id = str(uuid.uuid4())

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns the unofficial string representation of the class
        """
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def to_dict(self):
        """
        Returns a dictionary containing
        """
        new_dict = self.__dict__.copy()

        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time_frmt)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time_frmt)
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if "password" in new_dict:
            del new_dict["password"]

        return new_dict

    def save(self):
        """
        Modifies a record in the database
        """
        from models import storage

        self.updated_at = datetime.now(timezone.utc)
        storage.new(self)
        storage.save()

    def delete(self):
        """
        Deletes the current instance fro storage
        """
        from models import storage

        storage.delete(self)
