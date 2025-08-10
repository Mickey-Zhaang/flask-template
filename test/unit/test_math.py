"""
test_math.py
"""

from website.math import add, subtract


def test_add():
    """
    GIVEN two integer numbers
    WHEN we call add() from website.math
    THEN check the functionality of add()'
    """
    result = add(x=3, y=3)

    assert result == 6


def test_subtract():
    """
    GIVEN two integer numbers
    WHEN we call subtract() from website.math
    THEN check the functionality of subtract()'
    """
    pass
