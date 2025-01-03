#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the intersection_of_two function.
Contains comprehensive tests to ensure the correctness
of the intersection_of_two function.
It is designed to work with lists containing any data type allowed in a list.
Lists cannot be empty.

Test categories:

    - Standard cases: Lists with common items, lists with special characters.,
        lists with mixed data types,


    - Edge cases: Lists with no intersection, single-element lists, duplicated items,
        different types but equal values, lists with spaces items,
        sublist intersection, different case items

    - Defensive tests: Non-list inputs, one empty list, both empty lists

Created on 30-12-2024
Author: Linah Khayri
"""

import unittest

from ..intersection_of_two import intersection_of_two


class TestIntersectionOfTwo(unittest.TestCase):
    """Test suite for the intersection_of_two function that handles different cases."""

    # Standard cases

    def test_numbers_intersection(self):
        """Test intersection of two lists containing numbers (int or float)."""
        first_list = [1, 2, 3.6]
        second_list = [2, 3.6, 4]
        self.assertEqual(intersection_of_two(first_list, second_list), [2, 3.6])

    def test_strings_intersection(self):
        """Test intersection of two lists containing strings with common items."""
        first_list = ["apple", "banana", "cherry"]
        second_list = ["banana", "cherry", "orange"]
        self.assertEqual(
            intersection_of_two(first_list, second_list), ["banana", "cherry"]
        )

    def test_special_characters_intersection(self):
        """Test intersection of lists with special characters."""
        first_list = ["!", "@", "%", "&", "&"]
        second_list = ["*", "!", "&"]
        self.assertEqual(intersection_of_two(first_list, second_list), ["!", "&"])

    def test_mixed_types_intersection(self):
        """Test intersection of lists with mixed types (int, float, string, etc.)."""
        first_list = [1, "apple", 3.5, 4, "*"]
        second_list = ["apple", "*", 3.5, 2]
        self.assertEqual(
            intersection_of_two(first_list, second_list), ["apple", 3.5, "*"]
        )

    # Edge cases

    def test_no_intersection(self):
        """Test with no intersection; should return an empty list."""
        first_list = [1, 2, 3]
        second_list = [4, 5, 6]
        self.assertEqual(intersection_of_two(first_list, second_list), [])

    def test_single_element_lists_with_intersection(self):
        """Should return the list with the single item"""
        first_list = [1]
        second_list = [1]
        self.assertEqual(intersection_of_two(first_list, second_list), [1])

    def test_single_element_lists_no_intersection(self):
        """Should return an empty list."""
        first_list = [1]
        second_list = [2]
        self.assertEqual(intersection_of_two(first_list, second_list), [])

    def test_duplicated_items_intersection(self):
        """Should return the common duplicated item once"""
        first_list = [1, 2, 3, 3, 4]
        second_list = [3, 3, 5]
        self.assertEqual(intersection_of_two(first_list, second_list), [3])

    def test_duplicated_items_no_intersection(self):
        """Test lists with duplicated items and no intersection; should return an empty list."""
        first_list = [1, 2, 2, 3]
        second_list = [4, 4, 5]
        self.assertEqual(intersection_of_two(first_list, second_list), [])

    def test_different_types_but_equal_values(self):
        """Test when items have different types but equal values (e.g., int and whole float)."""
        first_list = [1, 2, 3.0]
        second_list = [3, 2, 1.0]
        self.assertEqual(intersection_of_two(first_list, second_list), [1, 2, 3.0])

    def test_sublist_intersection(self):
        """Test intersection when one list is a sublist of the other."""
        first_list = [1, 2, 3, 4, 5]
        second_list = [2, 3, 4]
        self.assertEqual(intersection_of_two(first_list, second_list), [2, 3, 4])

    def test_identical_lists(self):
        """Test when two identical lists are passed; should return the list itself."""
        first_list = [1, 2, 3]
        second_list = [1, 2, 3]
        self.assertEqual(intersection_of_two(first_list, second_list), [1, 2, 3])

    def test_spaces_intersection(self):
        """Test lists containing spaces as items; lists should handle spaces"""
        first_list = [" ", 2, 3]
        second_list = ["A", " ", " "]
        self.assertEqual(intersection_of_two(first_list, second_list), [" "])

    def test_different_case_intersection(self):
        """Test case-sensitivity in intersection (should not match 'HELLO' with 'hello')."""
        first_list = ["HELLO", "KITTY", 3]
        second_list = ["hello", "kitty", " "]
        self.assertEqual(intersection_of_two(first_list, second_list), [])

    # Defensive tests

    def test_one_empty_list(self):
        """Test when the one of the lists is empty."""
        first_list = []
        second_list2 = [1, 2, 3]
        with self.assertRaises(AssertionError):
            intersection_of_two(first_list, second_list2)

    def test_both_lists_empty(self):
        """Test when both lists are empty."""
        first_list = []
        second_list2 = []
        with self.assertRaises(AssertionError):
            intersection_of_two(first_list, second_list2)

    def test_any_non_list_input(self):
        """Test when any of the inputs is not a list."""
        first_list = "cat"
        second_list2 = []
        with self.assertRaises(AssertionError):
            intersection_of_two(first_list, second_list2)
