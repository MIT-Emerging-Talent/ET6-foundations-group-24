#!/usr/bin/env python3
# --#coding: utf-8 --
"""
Description: This file contains the test cases for the sum_range function.

The function sum_range(start, end) calculates the sum of all integers from
start to end (inclusive). And raises a TypeError if start or end is not
an integer.

Tests cases:
- standard test cases : test_positive_range, test_reversed_range,
test_single_number, test_negative_range, test_negative_range_reversed,
test_large_range, test_large_range_reversed
- Exception test cases : test_float_range, test_string_range, test_mixed_range
- Performance test cases : test_large_range, test_large_range_reversed
- Boundary test cases : test_single_number, test_negative_range,
-error test cases : test_float_range, test_string_range, test_mixed_range

date:2024-12-31
@author: Zeinab Mommed
"""

import unittest
from solutions.sum_range import sum_range


class TestSumRange(unittest.TestCase):
    """Tests for the sum_range function."""

    # Standard test cases
    def test_positive_range(self):
        """Test with a normal positive range."""
        self.assertEqual(sum_range(1, 5), 15)

    def test_reversed_range(self):
        """Test when start > end (reversed input)."""
        self.assertEqual(sum_range(5, 1), 15)

    # Boundary test cases
    def test_single_number(self):
        """Test a range with a single number."""
        self.assertEqual(sum_range(10, 10), 10)

    def test_negative_range(self):
        """Test a range that includes negative numbers."""
        self.assertEqual(sum_range(-3, 3), 0)

    def test_negative_range_reversed(self):
        """Test a range that includes negative numbers (reversed input)."""
        self.assertEqual(sum_range(3, -3), 0)

    def test_large_range(self):
        """Test with a large range."""
        self.assertEqual(sum_range(1, 100), 5050)

    def test_large_range_reversed(self):
        """Test with a large range."""
        self.assertEqual(sum_range(100, 1), 5050)

    # Defensive test cases
    def test_float_range(self):
        """Test with a range that includes floats."""
        with self.assertRaises(TypeError):
            sum_range(0.5, 3.5)

    def test_string_range(self):
        """Test with a range that includes strings."""
        with self.assertRaises(TypeError):
            sum_range("1", "5")

    def test_mixed_range(self):
        """Test with a range that includes a mix of strings and integers."""
        with self.assertRaises(TypeError):
            sum_range(1, "5")

    def test_error_range(self):
        """Test with a range that includes a mix of float and integers."""
        with self.assertRaises(TypeError):
            sum_range(1, 5.5)
