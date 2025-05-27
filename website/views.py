"""
views.py -- consists of any routes/pages visible to client
contains the logic handling and the rendering of html pages
"""

from flask import Blueprint, render_template

# initializing an exportable blueprint
main_blueprint = Blueprint("main", __name__)


# defining a "route" within our blueprint
@main_blueprint.route("/")
def index():
    """
    Landing Page
    """
    # renders the landing page "/"
    return render_template("index.html")
