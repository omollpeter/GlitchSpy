#!/usr/bin/python3
"""
This is module contains a class, Config - Defines secret key for
GlitchSpy application.
The secret key is important to prevent cross site request forgery
attacks (CSRF)
"""


import os


# Variables to interact with the database
GLITCHSPY_MYSQL_DB = os.environ.get("GLITCHSPY_MYSQL_DB")
GLITCHSPY_MYSQL_USER = os.environ.get("GLITCHSPY_MYSQL_USER")
GLITCHSPY_MYSQL_PWD = os.environ.get("GLITCHSPY_MYSQL_PWD")
GLITCHSPY_MYSQL_HOST = os.environ.get("GLITCHSPY_MYSQL_HOST")

DATABASE_URI = "mysql+mysqldb://{}:{}@{}/{}".format(
    GLITCHSPY_MYSQL_USER,
    GLITCHSPY_MYSQL_PWD,
    GLITCHSPY_MYSQL_HOST,
    GLITCHSPY_MYSQL_DB
)


class Config:
    """
    Contains the configuration settings for the application
    """
    SECRET_KEY = os.environ.get("GSPY_SECRET_KEY") or "secret_Key_for_GSpy"
    CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    WTF_CSRF_ENABLED = True
    DEBUG = True
    UPLOAD_FOLDER = os.path.realpath(".") + "/frontend/app/static/uploads"
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
