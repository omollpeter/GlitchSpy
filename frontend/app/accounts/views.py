#!/usr/bin/python3
"""
This script contains all the routes associated with accounts (user/
organization)
It also imports some modules from the flask library
    render_template - To render the defined templates in the applications
                        front-end
    flash - For displaying short lived messages
    redirects - To redirect to a different page after process completion
    url_for - To make managing url paths easier
"""


from flask import Blueprint
from flask import render_template, flash, redirect, url_for


accounts_bp = Blueprint("accounts", __name__, url_prefix="/gspy")



@accounts_bp.route("/login", methods=["GET", "POST"])
def login_page():
    """
    View function for the login page
    """
    return "<h1>Login page</h1>"


@accounts_bp.route("/register", methods=["GET", "POST"])
def signup_page():
    """
    View function for the registration page
    """
    return "<h1>Join Our Community</h1>"
