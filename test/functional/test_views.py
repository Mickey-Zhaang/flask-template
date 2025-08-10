"""
test_views.py
"""


def test_landing_page(mock_test_client):
    """
    GIVEN some client fixture
    WHEN '/' is requested
    THEN check validity request
    """
    response = mock_test_client.get("/")

    assert response.status_code == 200
    assert b"Welcome to Flask Template" in response.data
