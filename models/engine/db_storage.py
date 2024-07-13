#!/usr/bin/python3
"""
This module contains storage engine class - DBStorage
"""


from models.base_model import Base
from models.bug import Bug
from models.comment import Comment
from models.user import User
from models.organization import Organization
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


classes = {
    "Bug": Bug,
    "Comment": Comment,
    "User": User,
    "Organization": Organization
}

# Variables to interact with the database
GLITCHSPY_MYSQL_DB = os.environ.get("GLITCHSPY_MYSQL_DB")
GLITCHSPY_MYSQL_USER = os.environ.get("GLITCHSPY_MYSQL_USER")
GLITCHSPY_MYSQL_PWD = os.environ.get("GLITCHSPY_MYSQL_PWD")
GLITCHSPY_MYSQL_HOST = os.environ.get("GLITCHSPY_MYSQL_HOST")
GSPY_TYPE_STORAGE = os.environ.get("GSPY_TYPE_STORAGE")


class DBStorage:
    """
    Defines a storage class. This class is used to interact with
    database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiates the database engine
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            GLITCHSPY_MYSQL_USER,
            GLITCHSPY_MYSQL_PWD,
            GLITCHSPY_MYSQL_HOST,
            GLITCHSPY_MYSQL_DB
        ), pool_pre_ping=True)

    def reload(self):
        """
        Creates a new session for database interaction
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def new(self, obj):
        """
        Adds a new record to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Saves all the changes of the current database session
        """
        self.__session.commit()

    def all(self, cls=None):
        """
        Queries current database session to retrieve records from a
        specific table or all the tables
        """
        obj_dict = {}
        if not cls:
            for class_ in classes.values():
                objs = self.__session.query(class_).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    obj_dict[key] = obj
            return obj_dict
        objs = self.__session.query(cls).all()
        for obj in objs:
            key = obj.__class__.__name__ + "." + obj.id
            obj_dict[key] = obj

        return obj_dict

    def get(self, cls, id):
        """
        Retrieves and return a specific record from the database
        """
        if not cls:
            return None
        if cls not in classes.values():
            return None
        objs = self.all(cls)
        for obj in objs.values():
            if obj.id == id:
                return obj
        return None

    def count(self, cls=None):
        """
        Counts the number of records in a specific table or all tables
        """
        if not cls:
            return len(self.all())
        if cls not in classes.values():
            return 0
        return len(self.all(cls))

    def delete(self, obj=None):
        """
        Deletes a record from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def close(self):
        """
        Terminates the current database session
        """
        self.__session.remove()
