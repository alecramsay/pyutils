#!/usr/bin/env python3

"""
MISCELLANEOUS UTILITIES
"""


from pytest import approx
from typing import Any


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


# DON'T LIMIT WHAT GETS EXPORTED.

### END ###
