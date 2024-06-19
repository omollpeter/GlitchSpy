#!/usr/bin/python3
"""
This script handles the routes for users and bug statistics (count)
in the GlitchSpy application
"""


from models import storage
from models.user import User
from models.organization import Organization
from models.bug import Bug
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/stats")
def stats():
    """
    Returns the total number of bugs reported, users and organizations
    in the GlitchSpy application
    """
    classes = [Bug, User, Organization]
    names = ["bugs", "users", "organizations"]

    total = {}
    for i in range(len(classes)):
        total[names[i]] = storage.count(classes[i])
    return jsonify(total)
