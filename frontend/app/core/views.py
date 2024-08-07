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
from flask import render_template, flash, redirect, url_for, request, session
from markupsafe import escape
from frontend.app import db
from frontend.config import Config
from frontend.app.core.forms import BugForm, UpvoteForm
from frontend.app.core.models import Bug, Upvote
from flask_login import current_user




core_bp = Blueprint("core", __name__, url_prefix="/gspy")

# Define variable to hold allowed extensions for uploads
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif", "webp", "webm", "mp4", "avi", "mkv", "ogg"])

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
    return render_template("home.html", title="GlitchSpy")


@core_bp.route("/api", methods=["GET"])
def api_docs():
    """
    View function for the API documentation page
    """
    return render_template("api.html", title="GlitchSpy API")


@core_bp.route("/blog", methods=["GET"])
def blog_page():
    """
    View function the core_bplications blog page
    """
    return "<h1>Blog page</h1"

@core_bp.route("/about", methods=["GET"])
def about_page():
    """
    View function the core_bplications blog page
    """
    return render_template("about.html", title="About - GlitchSpy")


@core_bp.route("/bugreports", methods=["GET"])
def all_bug_reports():
    """
    View function for displaying all reported bugs
    """
    
    bugs = db.session.query(Bug).all()
    return render_template("bugs.html", title="Bug Reports", bugs=bugs)

@core_bp.route("/bugreports/<id>", methods=["GET"])
def view_bug(id):
    """
    View function for displaying a specific reported bug
    """
    id = escape(id)
    video_ext = ("webm", "mp4", "avi", "mkv")
    image_ext = ("png", "jpg", "jpeg", "gif", "webp")
    bug = db.session.query(Bug).filter_by(id=id).first()
    return render_template("bug.html", title="GlitchSpy - View Bug", bug=bug, id=id, form=UpvoteForm(), image=image_ext, video=video_ext)

@core_bp.route("/postbug", methods=["GET", "POST"])
def post_bug():
    """
    View function for creating a bug report page
    """
    form = BugForm()

    session["form_data"] = request.form
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        severity = form.severity.data
        product = form.product.data
        attachment = request.files.get("attachment") # Or form.attachment.data
        print(attachment.filename)
        if attachment and allowed_file(attachment.filename):
            attachment_name = secure_filename(attachment.filename)
            attachment.save(os.path.join(Config.UPLOAD_FOLDER, attachment_name))
            attachment_path = Config.UPLOAD_FOLDER + "/" + attachment_name
        else:
            attachment_path = ""
        description = form.description.data
        if current_user.is_authenticated:
            reportedBy = current_user.first_name + " " + current_user.last_name
        else:
            reportedBy = "anonymous"
        if not description:
            description = ""
        bug = Bug(
            name=name, category=category, severity=severity, product=product, attachment=attachment_path, reportedBy=reportedBy, description=description
        )

        db.session.add(bug)
        db.session.commit()
        flash("Bug reported successfully", "success")
        return redirect(url_for("core.view_bug", id=bug.id))
    return render_template("form-report.html", title="Report Bug", form=form)


@core_bp.route("/bugreports/<id>/upvote", methods=["POST"], strict_slashes=False)
def upvote(id):
    """Upvotes a bug"""
    form = UpvoteForm()
    id = escape(id)
    bug = db.session.query(Bug).filter_by(id=id).first()

    user = current_user.first_name + " " + current_user.last_name

    upvoted = db.session.query(Upvote).filter_by(bug_id=id, upvoted_by=user).first()
    if upvoted:
        bug.upvotes -= 1
        db.session.delete(upvoted)
        db.session.commit()
        class_name = "not-upvoted"
    else:
        bug.upvotes += 1
        new_upvote = Upvote(bug_id=id, upvoted_by=user)
        db.session.add(new_upvote)
        db.session.commit()
        class_name = "upvoted"

    return redirect(url_for("core.view_bug", id=bug.id, class_name=class_name))
