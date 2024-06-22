#!/usr/bin/python3
"""
This init file defines the application instance
"""


from flask import Flask
from frontend.config import Config

app = Flask(__name__)
app.config.from_object(Config)


# To prevent circular import error, import the routes module here
from frontend.app import routes