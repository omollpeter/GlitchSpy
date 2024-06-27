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


from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from frontend.app.accounts.forms import RegisterForm, LoginForm
from flask import g
from flask_login import current_user, login_user, logout_user, login_required
from frontend.app import login_manager, db
from .models import User
from hashlib import md5


accounts_bp = Blueprint("accounts", __name__, url_prefix="/gspy")



@login_manager.user_loader
def load_user(user_id):
    """
    Reloads the user object stored in the session
    """
    return User.query.get(user_id)

@accounts_bp.before_request
def get_current_user():
    g.user = current_user


@accounts_bp.route("/login", methods=["GET", "POST"])
def login_page():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        print(current_user.first_name + " " + current_user.last_name)
        return redirect(url_for("core.gspy_landing"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        password = md5(request.form["password"].encode()).hexdigest()

        if user and user.password == password:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("core.gspy_landing"))
        else:
            flash("Invalid email and/or password.", "danger")
            return render_template("login.html", form=form)
    return render_template("login.html", form=form)

@accounts_bp.route("/register", methods=["GET", "POST"])
def signup_page():
    if current_user.is_authenticated:
        flash("You are already registered.", "info")
        return redirect(url_for("core.gspy_landing"))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        if db.session.query(User).filter_by(email=form.email.data).first():
            flash("User is registered already")

        else:
            user = User(email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()

            login_user(user)
            flash("You registered and are now logged in. Welcome!", "success")

            return redirect(url_for("core.gspy_landing"))

    return render_template("signup.html", form=form)

@accounts_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("accounts.login_page"))
