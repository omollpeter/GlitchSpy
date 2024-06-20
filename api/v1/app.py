#!/usr/bin/python3
"""
This script starts a server for the application
It also contains views for handling errors
"""


from flask import Flask, jsonify, make_response
from flask_cors import CORS
from api.v1.views import app_views
from models import storage
import os


# Create the Flask instance 
app = Flask(__name__)

# Define a configuration that would ensure json is printed nicely
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

# Register the blueprint with the app
app.register_blueprint(app_views)

# Handle cross origin resource sharing
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) 


@app.teardown_appcontext
def close_db(exception=None):
    """
    Cleans up resources by terminating the current database session
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 Not Found error for the application
    """
    return make_response(jsonify({"error": "Not found"}), 404)


@app.errorhandler(400)
def error_400(error):
    """
    Handles all the errors associated with bad request
    """
    return make_response(jsonify({"error": error.description})), 400


if __name__ == "__main__":
    host = os.environ.get("GSPY_API_HOST", "0.0.0.0")
    port = os.environ.get("GSPY_API_PORT", "5000")

    app.run(host=host, port=port, threaded=True)
