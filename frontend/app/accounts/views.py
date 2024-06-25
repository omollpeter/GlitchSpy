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
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user
from frontend.app.accounts.forms import RegisterForm, LoginForm


accounts_bp = Blueprint("accounts", __name__, url_prefix="/gspy")


@accounts_bp.route("/login", methods=["GET", "POST"])
def login_page():
    """
    View function for the login page
    """
    form = LoginForm(request.form)
    return render_template("login.html", form=form)


@accounts_bp.route("/register", methods=["GET", "POST"])
def signup_page():
    """
    View function for the registration page
    """
    form = RegisterForm(request.form)
    return render_template("signup.html", form=form)


# @accounts_bp.route("/login", methods=["GET", "POST"])
# def login():
#     if current_user.is_authenticated:
#         flash("You are already logged in.", "info")
#         return redirect(url_for("core.home"))
#     form = LoginForm(request.form)
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and (user.password == request.form["password"]):
#             login_user(user)
#             return redirect(url_for("core.home"))
#         else:
#             flash("Invalid email and/or password.", "danger")
#             return render_template("login.html", form=form)
#     return render_template("login.html", form=form)

# @accounts_bp.route("/register", methods=["GET", "POST"])
# def register():
#     if current_user.is_authenticated:
#         flash("You are already registered.", "info")
#         return redirect(url_for("core.home"))
#     form = RegisterForm(request.form)
#     if form.validate_on_submit():
#         user = User(email=form.email.data, password=form.password.data)
#         db.session.add(user)
#         db.session.commit()

#         login_user(user)
#         flash("You registered and are now logged in. Welcome!", "success")

#         return redirect(url_for("core.home"))

#     return render_template("signup.html", form=form)
