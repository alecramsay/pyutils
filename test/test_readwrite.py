#!/usr/bin/env python3

"""
TEST I/O ROUTINES
"""

from pyutils import *

files_dir: str = "test/files/"
temp_dir: str = "temp/"


class TestReadWrite:
    def test_csv(self) -> None:
        # Typed read
        sample: str = "sample.csv"
        types: list = [str] + [int] * 9 + [float] * 2
        rows: list[dict] = read_csv(files_dir + sample, types)
        assert len(rows[0]) == 12
        assert len(rows) == 10

        # Write
        try:
            cols: list[str] = list(rows[0].keys())
            write_csv(temp_dir + sample, rows, cols)
            assert True
        except:
            assert False

        # Untyped read

        rows: list[dict] = read_csv(files_dir + sample)
        assert len(rows[0]) == 12
        assert len(rows) == 10

    def test_pickle(self) -> None:
        # Pickle
        sample: str = "sample.csv"
        types: list = [str] + [int] * 9 + [float] * 2
        rows: list[dict] = read_csv(files_dir + sample, types)
        try:
            write_pickle(temp_dir + sample, rows)
            assert True
        except:
            assert False

        # Unpickle
        try:
            unpickled: list = read_pickle(temp_dir + sample)
            assert True
        except:
            assert False

    def test_json(self) -> None:
        # Read
        sample: str = "sample.json"
        data: dict = read_json(files_dir + sample)
        assert len(data.keys()) == 6

        # Write
        try:
            write_json(temp_dir + sample, data)
            assert True
        except:
            assert False


### END ###
