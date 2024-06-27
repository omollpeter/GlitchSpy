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


import os
from werkzeug.utils import secure_filename
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from markupsafe import escape
from frontend.app import db
from frontend.config import Config
from frontend.app.core.forms import BugForm
from frontend.app.core.models import Bug
from flask_login import current_user




core_bp = Blueprint("core", __name__, url_prefix="/gspy")

# Define variable to hold allowed extensions for uploads
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif", "webp", "webm", "mp4", "avi", "mkv"])

def allowed_file(filename):
    """
    Returns whether or not a file can be uploaded or not
    """
    return "." in filename and filename.lower().rsplit(".", 1)[1] in\
     ALLOWED_EXTENSIONS


@core_bp.route("", methods=["GET"])
def gspy_landing():
    """
    View function for the GlitchSpy landing page
    """
    return render_template("home.html")


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
    form = BugForm()

    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        severity = form.severity.data
        product = form.product.data
        attachment = request.files.get("attachment") # Or form.attachment.data
        if attachment and allowed_file(attachment.filename):
            attachment = secure_filename(attachment.filename)
            attachment.save(os.path.join(Config.UPLOAD_FOLDER, attachment))
            attachment_path = Config.UPLOAD_FOLDER + "/" + attachment
        else:
            attachment_path = ""
        description = form.description.data
        if current_user.is_authenticated:
            reportedBy = current_user.first_name + " " + current_user.last_name
        else:
            reportedBy = "anonymous"
        bug = Bug(
            name=name, category=category, severity=severity, product=product, attachment=attachment_path, reportedBy=reportedBy
        )

        db.session.add(bug)
        db.session.commit()
        flash("Bug reported successfully")
        return redirect(url_for("core.view_bug", id=bug.id))
    return render_template("post_bug.html", form=form)
