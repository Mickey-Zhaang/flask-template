"""
__init__.py
"""

import os
from dotenv import load_dotenv
from flask import Flask
from website.views import main_blueprint

load_dotenv()


def create_app():
    """
    Create the weather app
    """
    app = Flask(__name__)

    # setting up secret key
    app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "lol_prob_not_getting_used"

    # register any blueprints
    app.register_blueprint(main_blueprint)

    return app
