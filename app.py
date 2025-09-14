"""
call 'python app.py' to start local host for testing
"""

from website import create_app

# utilizes the create_app() defined in app factory
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
