"""
App Factory i.e. the init of the website: accessed by app.py
"""

import os
from dotenv import load_dotenv
from flask import Flask
from .views import main_blueprint

load_dotenv()


def create_app():
    """
    The App Factory
    """
    app = Flask(__name__)

    # App Configurations
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    # Blueprints
    app.register_blueprint(main_blueprint)

    return app
