"""
call 'python app.py' to start local host for testing
"""

from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
