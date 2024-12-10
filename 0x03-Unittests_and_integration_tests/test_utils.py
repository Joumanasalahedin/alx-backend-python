#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns the expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path, expected_message):
        """Test access_nested_map raises KeyError with the expected message."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """Test suite for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url,
                      test_payload, mock_get):
        """Test get_json returns the expected result and calls requests.get"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)

        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test suite for the memoize decorator."""

    def test_memoize(self):
        """Test that memoize caches the result of a method."""

        class TestClass:
            """Test class"""

            def a_method(self):
                """Test a_method"""
                return 42

            @memoize
            def a_property(self):
                """test a_property"""
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=42) as mock_method:
            test_instance = TestClass()

            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)

            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
