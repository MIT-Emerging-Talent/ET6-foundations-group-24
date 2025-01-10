#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the is_anagram function.

Date created: Dec 31, 2024
Author: @Abel Teka

This test suite validates the behavior of the is_anagram function:
- It correctly identifies anagrams and non-anagrams.
- It handles case sensitivity and ignores spaces.
- It raises appropriate errors for invalid inputs.
"""

import unittest

from solutions.check_anagram import is_anagram


class TestIsAnagram(unittest.TestCase):
    """
    Unit tests for the is_anagram function, ensuring correctness
    and handling of edge cases and invalid inputs.
    """

    def test_anagram_positive_case(self):
        """Test with two strings that are anagrams."""
        self.assertTrue(is_anagram("listen", "silent"))

    def test_anagram_negative_case(self):
        """Test with two strings that are not anagrams."""
        self.assertFalse(is_anagram("hello", "world"))

    def test_anagram_case_insensitive(self):
        """Test with anagrams of different cases."""
        self.assertTrue(is_anagram("Listen", "Silent"))

    def test_anagram_with_spaces(self):
        """Test with anagrams containing spaces."""
        self.assertTrue(is_anagram("evil ", "vile"))

    def test_anagram_empty_strings(self):
        """Test with two empty strings."""
        self.assertTrue(is_anagram("", ""))

    def test_anagram_one_empty_string(self):
        """Test with one empty string and one non-empty string."""
        self.assertFalse(is_anagram("", "a"))

    def test_anagram_special_characters(self):
        """Test with strings containing special characters."""
        self.assertFalse(is_anagram("evil!", "vile"))

    def test_anagram_numeric_values(self):
        """Test with numeric strings."""
        self.assertFalse(is_anagram("123", "321a"))

    def test_invalid_input_not_string(self):
        """Test for AttributeError when inputs are not strings."""
        with self.assertRaises(AttributeError):
            is_anagram(["list"], "silent")
        with self.assertRaises(AttributeError):
            is_anagram("listen", 123)

    def test_anagram_boundary_case_spaces(self):
        """Test with strings that are spaces."""
        self.assertTrue(is_anagram("   ", "   "))

    def test_anagram_boundary_case_identical_strings(self):
        """Test with two identical strings."""
        self.assertTrue(is_anagram("same", "same"))


if __name__ == "__main__":
    unittest.main()
