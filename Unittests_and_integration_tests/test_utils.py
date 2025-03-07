#!/usr/bin/env python3
"""Script contains tests for utils.py functions"""
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Class contains test method(s) fro access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any):
        """Method tests if access_nested_map returns correct output"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, key: str):
        """Method tests whether exceptions are handled correctly"""

        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)

        self.assertEqual(str(cm.exception), repr(key))


if __name__ == "__main__":
    unittest.main()
