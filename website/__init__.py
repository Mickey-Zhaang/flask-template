"""
__init__.py: The "App factory"
"""

import os
from dotenv import load_dotenv
from flask import Flask

# blueprints
from website.views import main_blueprint

# loads environmental variables from .env
load_dotenv()


def create_app():
    """
    Create a basic Flask Application
    """
    app = Flask(__name__)

    # setting up secret key
    app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "lol_prob_not_getting_used"

    # register any blueprints
    app.register_blueprint(main_blueprint)

    return app
