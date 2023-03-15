#!/usr/bin/env python3

"""
TEST EQUALITY UTILITIES
"""

from pyutils import *


class TestEqual:
    def test_dict_approx_equal(self) -> None:
        d1: dict[str, Any] = {"A": "1", "B": 2, "C": 3.14}

        d2: dict[str, Any] = {"A": "1", "B": 2, "C": 3.14}
        assert dict_approx_equal(d1, d2)

        d2 = {"A": "1", "B": 2, "C": 3.1400001}
        assert dict_approx_equal(d1, d2)

        d2 = {"A": "1", "B": 2, "C": 3.2}
        assert not dict_approx_equal(d1, d2)

        d2 = {"A": "1", "B": 3, "C": 3.14}
        assert dict_approx_equal(d1, d2, int_threshold=1)


### END ###
