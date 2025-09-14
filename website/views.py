"""
views.py: defining routes/pages for user flow by rendering templates/html files
    i.e. the main landing page defined by the route "/" below
"""

from flask import Blueprint, render_template

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    """
    Main landing page
    """
    return render_template("index.html")
