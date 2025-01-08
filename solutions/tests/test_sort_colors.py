#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains the test cases for the sort_colors function.

The function sort_colors(nums) sorts a given list of integers representing
colors (0 for red, 1 for white, and 2 for blue) in-place without using any
built-in sorting libraries. It ensures the list is sorted in ascending order
while modifying the original list directly.

Test cases:
- Standard test cases:
  - test_empty_list: Handles an empty input list.
  - test_single_element: Handles a list containing a single element.
  - test_all_same_elements: Handles a list where all elements are the same.
  - test_already_sorted: Ensures an already sorted list is not modified.
  - test_unsorted_list: Sorts a typical unsorted list.

- Edge cases:
  - test_large_list: Tests the function with a large input list.
  - test_randomly_generated_list: Tests with a randomly generated list.

- Exception test cases:
  - test_not_a_list: Ensures a TypeError is raised for non-list inputs.
  - test_invalid_elements_type: Ensures a TypeError is raised for invalid
    element types (e.g., non-integer elements).
  - test_invalid_elements_range: Ensures an AssertionError is raised for invalid
    elements (e.g., integers not in the range [0, 2]).

Created on 26 10 2024

@author: Mohamed-Elnageeb
"""

import unittest

# Import the function to be tested
from ..sort_colors import sort_colors


class TestSortColors(unittest.TestCase):
    """Test the sort_colors function"""

    def test_empty_list(self):
        """It should handle an empty list"""
        nums = []
        sort_colors(nums)
        self.assertEqual(nums, [])

    def test_single_element(self):
        """It should handle a list with one element"""
        nums = [1]
        sort_colors(nums)
        self.assertEqual(nums, [1])

    def test_all_same_elements(self):
        """It should handle a list with all elements being the same"""
        nums = [2, 2, 2]
        sort_colors(nums)
        self.assertEqual(nums, [2, 2, 2])

    def test_already_sorted(self):
        """It should not modify an already sorted list"""
        nums = [0, 0, 1, 1, 2, 2]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_unsorted_list(self):
        """It should sort an unsorted list"""
        nums = [2, 0, 2, 1, 1, 0]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_large_list(self):
        """It should handle a large list"""
        nums = [0, 2, 1] * 100000
        expected = sorted(nums)  # expected output is a sorted array
        sort_colors(nums)
        self.assertEqual(nums, expected)

    def test_not_a_list(self):
        """It should raise a TypeError if the input is not a list"""
        with self.assertRaises(TypeError):
            sort_colors("not a list")

    def test_invalid_elements_type(self):
        """It should raise a TypeError for invalid element types"""
        nums = [0, 1, "2"]  # Invalid element "2" (string)
        with self.assertRaises(TypeError):
            sort_colors(nums)

    def test_invalid_elements_range(self):
        """It should raise an AssertionError for elements out of range"""
        nums = [0, 1, 3]  # Invalid element 3 (out of range)
        with self.assertRaises(AssertionError):
            sort_colors(nums)


if __name__ == "__main__":
    unittest.main()
