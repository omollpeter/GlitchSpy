#!/usr/bin/python3
"""
This script handles bug related routes
"""


from models import storage
from models.bug import Bug
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route("/bugs", methods=["GET"], strict_slashes=False)
def get_bugs():
    """
    Retrieves all reported bugs with a public status
    """
    bugs = storage.all(Bug)

    bug_list = []
    for bug in bugs.values():
        if bug.status == "public":
            bug_list.append(bug.to_dict())

    return jsonify(bug_list)
