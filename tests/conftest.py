"""
Defines Testing Fixtures: Conftest.py
    Fixtures are like reusable components in subdirectories i.e. a client fixture
    To run all tests, run `python tests/run_tests.py`

Also Note*
    TDD - "Test Driven Development" is a concept of writing tests before the code itself
    Not really practical when dealing with new APIs and such where behavior is unfamiliar...
    But very useful as it forces you to think about your logic before actually writing it out
    - also, forces you to write testable code through a refactoring cycle :)
"""

# We will be using the Pytest Library
import pytest
from website import create_app


@pytest.fixture
def app():
    """
    A Testing App Instance
    """
    app = create_app()

    # Setting up configurations just like in app factory
    app.config["TESTING"] = True

    # Configures the app to show raw exceptions for debugging
    app.config["PROPAGATE_EXCEPTIONS"] = False

    # Don't need a really secret key for testing
    app.config["SECRET_KEY"] = "secret"

    yield app


@pytest.fixture(scope="function")
def client(app):
    """
    Pytest Fixture:
        Fixture Name: client
        Scope: function
        Yields a client for testing!
    """
    # Uses the app context to yield a testing client
    with app.test_client() as test_client:
        yield test_client
