#!/usr/bin/python3
"""
This module contains all the routes for GlitchSpy app
It also imports some modules from the flask library
    render_template - To render the defined templates in the applications
                        front-end
    flash - For displaying short lived messages
    redirects - To redirect to a different page after process completion
    url_for - To make managing url paths easier

    escape (from markupsafe) - Prevents injection attacks
"""


from frontend.app import app
from flask import render_template, flash, redirect, url_for
from markupsafe import escape


@app.route("/gspy", methods=["GET"], strict_slashes=False)
def gspy_landing():
    """
    View function for the GlitchSpy landing page
    """
    return "<h1>Landing page</h1>"


@app.route("/gspy/login", methods=["GET", "POST"])
def login_page():
    """
    View function for the login page
    """
    return "<h1>Login page</h1>"


@app.route("/gspy/register", methods=["GET", "POST"], strict_slashes=False)
def signup_page():
    """
    View function for the registration page
    """
    return "<h1>Join Our Community</h1>"


@app.route("/gspy/api", methods=["GET"], strict_slashes=False)
def api_docs():
    """
    View function for the API documentation page
    """
    return "<h1>API Documentation</h1>"


@app.route("/gspy/blog", methods=["GET"], strict_slashes=False)
def blog_page():
    """
    View function the applications blog page
    """
    return "<h1>Blog page</h1"


@app.route("/gspy/bugreports", methods=["GET"], strict_slashes=False)
def all_bug_reports():
    """
    View function for displaying all reported bugs
    """
    return "<h1>Bug reports</h1>"

@app.route("/gspy/bugreports/<id>", methods=["GET"], strict_slashes=False)
def view_bug(id):
    """
    View function for displaying a specific reported bug
    """
    id = escape(id)
    return "<h1>Bug report</h1>"

@app.route("/gspy/postbug", methods=["GET", "POST"], strict_slashes=False)
def post_bug():
    """
    View function for creating a bug report page
    """
    return "<h1>Report Bug</h1>"
