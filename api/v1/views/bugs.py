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
            bug_comments = bug.comments()
            comment_strings = []
            for comm in bug_comments:
                comment_strings.append(comm.to_dict()["comment_string"])
            bug_dict = bug.to_dict()
            bug_dict["comments"] = comment_strings
            bug_list.append(bug_dict)
            # bug_list.append(bug.to_dict())

    return jsonify(bug_list)


@app_views.route("/bugs/<bug_id>", methods=["GET"], strict_slashes=False)
def get_bug(bug_id):
    """
    Retrieves a specific bug
    """
    bug = storage.get(Bug, bug_id)
    if not bug:
        abort(404)

    if bug.status == "public":
        bug_dict = bug.to_dict()

        bug_comments = bug.comments()
        comment_strings = []
        for comm in bug_comments:
            comment_strings.append(comm.to_dict()["comment_string"])

        bug_dict["comments"] = comment_strings

        return jsonify(bug_dict)
    abort(404)


@app_views.route("/bugs/<bug_id>", methods=["DELETE"], strict_slashes=False)
def delete(bug_id):
    """
    Deletes a bug report provided the user is authenticated
    """
    bug = storage.get(Bug, bug_id)
    if not bug:
        abort(404)

    storage.delete(bug)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route("/bugs/<bug_id>", methods=["PUT"], strict_slashes=False)
def update_bug(bug_id):
    """
    Updates a bug report
    """
    bug = storage.get(Bug, bug_id)
    if not bug:
        abort(404)
    
    data = request.get_json()
    if not data:
        abort(400, "Not JSON data")
    
    ignored_keys = ["id", "updated_at", "created_at"]

    for key, value in data.items():
        if key not in ignored_keys:
            setattr(bug, key, value)

    storage.save()
    return make_response(jsonify(bug.to_dict()), 200)


@app_views.route("/bugs", methods=["POST"], strict_slashes=False)
def create_bug_report():
    """
    Creates a new bug report
    """
    data = request.get_json()
    if not data:
        abort(400, "Not JSON data")

    attrs = [
        "name", "description", "category", "severity", "product",
        "attachment"
    ]

    if not data.get("name"):
        abort(400, "Missing name")

    if not data.get("category"):
        abort(400, "Missing category")

    if not data.get("severity"):
        abort(400, "Missing severity")
    
    if not data.get("product"):
        abort(400, "Missing product")

    for key in data.keys():
        if key not in attrs:
            del data[key]

    data["reportedBy"] = "anonymous"
    data["status"] = "public"

    bug = Bug(**data)
    bug.save()

    return make_response(jsonify(bug.to_dict())), 201
    