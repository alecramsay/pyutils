#!/usr/bin/env python3

"""
TEST I/O ROUTINES
"""

from pyutils import *

files_dir: str = "test/files/"
temp_dir: str = "temp/"


class TestReadWrite:
    def test_csv(self) -> None:
        sample: str = "sample.csv"
        types: list = [str] + [int] * 9 + [float] * 2
        rows: list[dict] = read_csv(files_dir + sample, types)
        assert len(rows[0]) == 12
        assert len(rows) == 10

        try:
            cols: list[str] = list(rows[0].keys())
            write_csv(temp_dir + sample, rows, cols)
            assert True
        except:
            assert False


### END ###
