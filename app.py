"""
Access Point: run `python app.py` to build the app and run on local host
"""

from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
