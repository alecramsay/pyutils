#!/usr/bin/env python3

"""
ROUGH EQUALITY UTILITIES
"""


from pytest import approx
from typing import Any


def roughly_equal(x: float, y: float) -> bool:
    """Check if two floats are approximately equal"""

    return x == approx(y)


def dict_approx(actual: dict, expected: dict) -> bool:
    """Check if two dictionaries are approximately equal"""

    for key in expected:
        if key not in actual:
            return False

        a: Any = actual[key]
        e: Any = expected[key]

        if type(e) == float:
            if a != approx(e):
                return False
        else:
            if a != e:
                return False

    return True


def dict_close(actual: dict, expected: dict, threshold: int = 1) -> bool:
    """Close but not necessarily equal"""

    for key in expected:
        if key not in actual:
            return False

        if type(expected[key]) == str:
            if actual[key] != expected[key]:
                return False

        if type(expected[key]) == int:
            # Allow for rounding differences
            if abs(actual[key] - expected[key]) > threshold:
                return False

        if type(expected[key]) == float:
            if actual[key] != approx(expected[key]):
                return False

    return True


# DON'T LIMIT WHAT GETS EXPORTED.

### END ###
