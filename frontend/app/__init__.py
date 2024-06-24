#!/usr/bin/python3
"""
This init file defines the application instance
"""


from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager # This lets applicatiom and Flask-login work together
from app.accounts.models import User

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True

# Navigate to resource with or without trailing slash
app.url_map.strict_slashes = False

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "accounts.login" # Refers to the funcyion that will handle login process 
login_manager.login_message_category = "danger" # Customizes message category
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# To prevent circular import error, import the routes module here
from app.accounts.views import accounts_bp


# Register blueprints
app.register_blueprint(accounts_bp)


@login_manager.user_loader
def load_user(user_id):
    """
    Reloads the user object stored in the session
    """
    return User.query.filter(User.id == str(user_id)).first()
