"""
(Functional)
test_views.py:  End to End Testing: tests the entire system from the client's POV
                Think about it like testing functionality of routes/pages defined in views.py
tests:
    - testing_landing_page
"""


# ALWAYS write the doc string for a test in this format
def test_landing_page(client):
    """
    GIVEN some client
    WHEN '/' is requested (GET)
    THEN check the functionality of the route
    """
    response = client.get("/")  # A GET request

    # check success status
    assert response.status_code == 200

    # response.data is in bytes, check to see if title in the response data
    assert b"Flask Template" in response.data

    # additionally check other elements in the rendered html (Optional)
    assert b"Welcome to My Flask App" in response.data
