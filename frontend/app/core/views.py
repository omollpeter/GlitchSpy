#!/usr/bin/python3
"""
This module contains the routes for all core functionalities and their
corresponding view functions
It also imports some modules from the flask library
    render_template - To render the defined templates in the applications
                        front-end
    flash - For displaying short lived messages
    redirects - To redirect to a different page after process completion
    url_for - To make managing url paths easier

    escape (from markupsafe) - Prevents injection attacks
"""


from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from markupsafe import escape


core_bp = Blueprint("core", __name__, url_prefix="/gspy")


@core_bp.route("", methods=["GET"])
def gspy_landing():
    """
    View function for the GlitchSpy landing page
    """
    return "<h1>Landing page</h1>"


@core_bp.route("/api", methods=["GET"])
def api_docs():
    """
    View function for the API documentation page
    """
    return "<h1>API Documentation</h1>"


@core_bp.route("/blog", methods=["GET"])
def blog_page():
    """
    View function the core_bplications blog page
    """
    return "<h1>Blog page</h1"


@core_bp.route("/bugreports", methods=["GET"])
def all_bug_reports():
    """
    View function for displaying all reported bugs
    """
    return "<h1>Bug reports</h1>"

@core_bp.route("/bugreports/<id>", methods=["GET"])
def view_bug(id):
    """
    View function for displaying a specific reported bug
    """
    id = escape(id)
    return "<h1>Bug report</h1>"

@core_bp.route("/postbug", methods=["GET", "POST"])
def post_bug():
    """
    View function for creating a bug report page
    """
    return "<h1>Report Bug</h1>"
