#!/usr/bin/python3
"""
This is module contains a class, Config - Defines secret key for
GlitchSpy application.
The secret key is important to prevent cross site request forgery
attacks (CSRF)
"""


import os


class Config:
    """
    Contains the secret key for the application
    """
    SECRET_KEY = os.environ.get("GSPY_SECRET_KEY") or "secret_Key_for_GSpy"
