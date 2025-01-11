#!/usr/bin/env python3
# -- coding: utf-8 --

"""
This module contains unit tests for the `find_maximum_minimum` function.
The `find_maximum_minimum` function is tested for various scenarios including
standard cases, edge cases such as an empty list, and invalid inputs.

These tests help ensure that the function behaves correctly and handles edge cases.

@author: Yonatan Y. Yifat
"""

import unittest

from solutions.finding_maximum_minimum import find_maximum_minimum


class TestFindingMaximumMinimum(unittest.TestCase):
    """Test suite for the find_maximum_minimum function."""

    def test_positive_numbers(self):
        """Test with a list of positive numbers."""
        numbers = [5, 10, 15, 20]
        self.assertEqual(find_maximum_minimum(numbers), (5, 20))

    def test_negative_numbers(self):
        """Test with a list of negative numbers."""
        numbers = [-5, -10, -15, -20]
        self.assertEqual(find_maximum_minimum(numbers), (-20, -5))

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers."""
        numbers = [-5, 10, 15, -20]
        self.assertEqual(find_maximum_minimum(numbers), (-20, 15))

    def test_single_number(self):
        """Test with a list containing a single number."""
        numbers = [7]
        self.assertEqual(find_maximum_minimum(numbers), (7, 7))

    def test_identical_numbers(self):
        """Test with a list of identical numbers."""
        numbers = [10, 10, 10]
        self.assertEqual(find_maximum_minimum(numbers), (10, 10))

    def test_floats(self):
        """Test with a list containing float numbers."""
        numbers = [1.5, 2.5, 3.5, 4.5]
        self.assertEqual(find_maximum_minimum(numbers), (1.5, 4.5))

    def test_empty_list(self):
        """Test with an empty list, should raise ValueError."""
        with self.assertRaises(ValueError):
            find_maximum_minimum([])

    def test_non_numeric_elements(self):
        """Test with a list containing non-numeric elements, should raise ValueError."""
        with self.assertRaises(ValueError):
            find_maximum_minimum([1, "a", 3])

    def test_invalid_input_type(self):
        """Test with a non-list input, should raise ValueError."""
        with self.assertRaises(ValueError):
            find_maximum_minimum(None)

    def test_strings_in_list(self):
        """Test with a list of strings, should raise ValueError."""
        with self.assertRaises(ValueError):
            find_maximum_minimum(["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
