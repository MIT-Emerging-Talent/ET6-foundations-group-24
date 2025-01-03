#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the count_distinct_subsequences function.
Contains comprehensive tests to ensure the correctness
of the count_distinct_subsequences function.

Test categories:
    - Standard cases: Common strings with matching subsequences,
    non-matching strings.
    - Edge cases: Empty t string, empty s string,
    both strings empty, repeated characters.
    - Performance tests: Large strings to verify efficiency with memoization.
    - Defensive tests: Non-string inputs, invalid types for s and t.

Created on 02 01 2025
Author: Mohamed-Elnageeb
"""

import unittest

from ..distinct_subsequences import count_distinct_subsequences


class TestCountDistinctSubsequences(unittest.TestCase):
    """Test suite for the count_distinct_subsequences function."""

    # Standard cases

    def test_matching_subsequence(self):
        """Test matching subsequences in typical strings."""
        s = "rabbbit"
        t = "rabbit"
        self.assertEqual(count_distinct_subsequences(s, t), 3)

    def test_no_matching_subsequence(self):
        """Test when there are no matching subsequences."""
        s = "abc"
        t = "def"
        self.assertEqual(count_distinct_subsequences(s, t), 0)

    def test_full_match(self):
        """Test when s matches t exactly."""
        s = "abc"
        t = "abc"
        self.assertEqual(count_distinct_subsequences(s, t), 1)

    # Edge cases

    def test_empty_target(self):
        """Test when the t string is empty (always one way to match)."""
        s = "abc"
        t = ""
        self.assertEqual(count_distinct_subsequences(s, t), 1)

    def test_empty_source(self):
        """Test when the s string is empty (cannot match anything)."""
        s = ""
        t = "abc"
        self.assertEqual(count_distinct_subsequences(s, t), 0)

    def test_both_empty(self):
        """Test when both s and t strings are empty."""
        s = ""
        t = ""
        self.assertEqual(count_distinct_subsequences(s, t), 1)

    def test_repeated_characters(self):
        """Test with repeated characters in s and t."""
        s = "aaa"
        t = "aa"
        self.assertEqual(count_distinct_subsequences(s, t), 3)

    # Performance tests

    def test_large_strings(self):
        """Test with large strings to verify efficiency."""
        s = "a" * 1000
        t = "a" * 10
        result = count_distinct_subsequences(s, t)
        self.assertGreater(result, 0)  # Ensure it computes without errors

    # Defensive tests

    def test_non_string_source(self):
        """Test when s is not a string."""
        s = 123
        t = "abc"
        with self.assertRaises(AssertionError):
            count_distinct_subsequences(s, t)

    def test_non_string_target(self):
        """Test when t is not a string."""
        s = "abc"
        t = [1, 2, 3]
        with self.assertRaises(AssertionError):
            count_distinct_subsequences(s, t)

    def test_both_non_strings(self):
        """Test when both s and t are not strings."""
        s = 123
        t = 456
        with self.assertRaises(AssertionError):
            count_distinct_subsequences(s, t)


if __name__ == "__main__":
    unittest.main()
