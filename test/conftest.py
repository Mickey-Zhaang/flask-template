"""
Defines fixtures and potentially dummy classes for unit testing later on
"""

import os
import pytest
from website import create_app


@pytest.fixture(scope="module")
def app():
    """
    testing app: the template for the testing fixture
    """
    os.environ["CONFIG_TYPE"] = "config.TestingConfig"
    flask_app = create_app()
    with flask_app.app_context():
        yield flask_app


@pytest.fixture
def mock_test_client(app):
    """
    mock client: utilizing the template above, build the actual test client
    """
    return app.test_client()
