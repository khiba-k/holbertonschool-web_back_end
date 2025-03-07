#!/usr/bin/env python3
"""Script contains tests for utils.py functions"""
import utils
from utils import access_nested_map, get_json
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """Class defines method(s) that test get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url: str, test_payload: Dict,
                      mock_get: Mock) -> None:
        """Method tests if get_json returns correct output"""
        mock_get.return_value.json.return_value = test_payload

        result = get_json(test_url)

        self.assertEqual(result, test_payload)
        mock_get.assert_called_with(test_url)


if __name__ == "__main__":
    unittest.main()
