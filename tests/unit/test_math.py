"""
(Unit)
test_math.py: tests "math.py" module in an isolated environment i.e. unit testing

tests:
    - test_add
    - test_subtract
"""

from website.math import add, subtract


def test_add():
    """
    GIVEN add() from math.py
    WHEN add() is called
    TEST functionality
    """
    result = add(2, 2)

    # assert our result is true
    assert result == 4


def test_subtract():
    """
    GIVEN subtract() from math.py
    WHEN subtract() is called
    TEST functionality
    """
    pass  # Try writing one yourself, reference the math.py and recreate the above structure
