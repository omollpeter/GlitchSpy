#!/usr/bin/python3
"""
This module contains Blueprint for the GlitchSpy API
"""


from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix="/api/gspy/v1")


from api.v1.views.index import *
from api.v1.views.bugs import *
