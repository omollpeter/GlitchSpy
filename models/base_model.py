#!/usr/bin/python3
"""
This module contains class definition for the base model - BaseModel
All data models created for this app will inherit from the BaseModel
"""


from datetime import datetime, timezone
from models import storage
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


# Define a time format string
time_frmt = "%Y-%m-%dT%H:%M:%S.%f"

# Define a declarative_base class to map our models to a database table
Base = declarative_base()


class BaseModel:
    """
    Defines a base model class. All models subclasses of this class
    """
    id = Column(String(60), primary_key=True, default=uuid.uuid4())
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))

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

        return new_dict

    def save(self):
        """
        Modifies a record in the database
        """
        self.updated_at = datetime.now(timezone.utc)
        storage.new(self)
        storage.save()
