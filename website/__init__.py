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

    app.register_blueprint(main_blueprint)

    return app
