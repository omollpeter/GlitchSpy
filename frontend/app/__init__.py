#!/usr/bin/python3
"""
This init file defines the application instance
"""


from models import storage
from models.user import User
from flask import Flask
from frontend.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager # This lets applicatiom and Flask-login work together

app = Flask(__name__)
app.config.from_object(Config)

# Navigate to resource with or without trailing slash
app.url_map.strict_slashes = False

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "accounts.login_page" # Refers to the funcyion that will handle login process 
login_manager.login_message_category = "danger" # Customizes message category
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# To prevent circular import error, import the routes module here
from frontend.app.accounts.views import accounts_bp
from frontend.app.core.views import core_bp


# Register blueprints
app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)

with app.app_context():
    db.create_all()
