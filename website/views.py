"""
views.py: defining routes/pages for user flow
    i.e. index or "/" is the default route which we can treat as the Landing Page
"""

from flask import Blueprint, render_template

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    """
    Main landing page
    """
    return render_template("index.html")
