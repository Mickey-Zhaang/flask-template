"""
Access Point: run `python app.py` to build the app and run on local host
"""

# accessing the app factory
from website import create_app

# creating the app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
