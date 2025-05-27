"""
App Factory i.e. the init of the website: accessed by app.py
"""

# dealing with imports
import os
from dotenv import load_dotenv
from flask import Flask
from .views import main_blueprint

# loads our .env file
load_dotenv()

# the app factory
def create_app():
    """
    The App Factory
    """
    app = Flask(__name__)

    # App Configurations
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    # Registering Blueprints
    app.register_blueprint(main_blueprint)

    return app
