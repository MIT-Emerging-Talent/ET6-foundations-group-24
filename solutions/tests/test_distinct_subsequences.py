#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the distinct_subsequences function.
Contains comprehensive tests to ensure the correctness
of the distinct_subsequences function.

Test categories:
    - Standard cases: Common strings with matching subsequences,
    non-matching strings.
    - Edge cases: Empty target_str string, empty source_str string,
    both strings empty, repeated characters.
    - Performance tests: Large strings to verify efficiency with memoization.
    - Defensive tests: Non-string inputs, invalid types for
    source_str and target_str.

Notes on Memoization:
    - The distinct_subsequences function uses the @cache decorator to store
    previously computed results for specific subproblems.
    - This avoids redundant computations for overlapping subproblems,
    significantly reducing the time complexity
    from exponential to polynomial.
    - The performance tests verify that the implementation efficiently handles
    large input sizes, which would otherwise be
    infeasible without memoization.

Created on 02 01 2025
Author: Mohamed-Elnageeb
"""

import unittest

from ..distinct_subsequences import distinct_subsequences


class TestCountDistinctSubsequences(unittest.TestCase):
    """Test suite for the distinct_subsequences function."""

    # Standard cases
    def test_matching_subsequence(self):
        """Test matching subsequences in typical strings."""
        source_str = "rabbbit"
        target_str = "rabbit"
        self.assertEqual(distinct_subsequences(source_str, target_str), 3)

    def test_no_matching_subsequence(self):
        """Test when there are no matching subsequences."""
        source_str = "abc"
        target_str = "def"
        self.assertEqual(distinct_subsequences(source_str, target_str), 0)

    def test_full_match(self):
        """Test when source_str matches target_str exactly."""
        source_str = "abc"
        target_str = "abc"
        self.assertEqual(distinct_subsequences(source_str, target_str), 1)

    # Edge cases

    def test_empty_target(self):
        """Test when the target_str is empty (always one way to match)."""
        source_str = "abc"
        target_str = ""
        self.assertEqual(distinct_subsequences(source_str, target_str), 1)

    def test_empty_source(self):
        """Test when the source_str is empty (cannot match anything)."""
        source_str = ""
        target_str = "abc"
        self.assertEqual(distinct_subsequences(source_str, target_str), 0)

    def test_both_empty(self):
        """Test when both source_str and target_str are empty."""
        source_str = ""
        target_str = ""
        self.assertEqual(distinct_subsequences(source_str, target_str), 1)

    def test_repeated_characters(self):
        """Test with repeated characters in source_str and target_str."""
        source_str = "aaa"
        target_str = "aa"
        self.assertEqual(distinct_subsequences(source_str, target_str), 3)

    def test_with_special_characters(self):
        """Test with special characters in source_str and target_str."""
        source_str = "a aa,,b"
        target_str = "a ,b"
        self.assertEqual(distinct_subsequences(source_str, target_str), 2)

    def test_case_sensitivity(self):
        """Test case sensitivity in source_str and target_str."""
        source_str = "aB BAGBB"
        target_str = "AB"
        self.assertEqual(distinct_subsequences(source_str, target_str), 2)

    # Performance tests

    def test_large_strings(self):
        """Test with large strings to verify efficiency."""
        source_str = "a" * 1000
        target_str = "a" * 10
        result = distinct_subsequences(source_str, target_str)
        self.assertEqual(
            result, 263409560461970212832400
        )  # number of ways to choose 10 a's from 1000 a's

    # Defensive tests

    def test_non_string_source(self):
        """Test when source_str is not a string."""
        source_str = 123
        target_str = "abc"
        with self.assertRaises(TypeError):
            distinct_subsequences(source_str, target_str)

    def test_non_string_target(self):
        """Test when target_str is not a string."""
        source_str = "abc"
        target_str = [1, 2, 3]
        with self.assertRaises(TypeError):
            distinct_subsequences(source_str, target_str)

    def test_both_non_strings(self):
        """Test when both source_str and target_str are not strings."""
        source_str = 123
        target_str = True
        with self.assertRaises(TypeError):
            distinct_subsequences(source_str, target_str)


if __name__ == "__main__":
    unittest.main()
