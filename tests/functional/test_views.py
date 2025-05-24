"""
(Functional)
test_views.py: tests functionality of routes/pages defined in views.py i.e. functional testing

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
    response = client.get("/")  # A GET method

    # check success status
    assert response.status_code == 200

    # response.data is in bytes, check to see if title in the data
    assert b"Flask Template" in response.data

    # additionally check other elements in the rendered html (Optional)
    assert b"Welcome to My Flask App" in response.data
