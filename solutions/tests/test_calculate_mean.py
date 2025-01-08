#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the calculate_mean function.

Date created: Dec 30, 2024
Author: @Abel Teka

This test suite validates the calculate_mean function's behavior, ensuring it:
- Correctly calculates the mean for positive, negative, and mixed numbers.
- Handles edge cases such as empty lists, single elements, and zeros.
- Allows infinity as a valid mean result.
- Performs reliably with large and small numeric values.

Each test case is designed to ensure a single assertion, with clear documentation for behavior and expectations.
"""

import unittest

from solutions.calculate_mean import calculate_mean


class TestCalculateMean(unittest.TestCase):
    """Unit tests for the calculate_mean function."""

    def test_positive_numbers(self):
        """Test mean calculation with a list of positive numbers."""
        self.assertEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0)

    def test_negative_numbers(self):
        """Test mean calculation with a list of negative numbers."""
        self.assertEqual(calculate_mean([-1, -2, -3, -4, -5]), -3.0)

    def test_mixed_numbers(self):
        """Test mean calculation with a mix of positive and negative numbers."""
        self.assertEqual(calculate_mean([-10, 0, 10]), 0.0)

    def test_single_number(self):
        """Test mean calculation with a single number."""
        self.assertEqual(calculate_mean([42]), 42.0)

    def test_floating_point_numbers(self):
        """Test mean calculation with a list of floating-point numbers."""
        self.assertAlmostEqual(calculate_mean([1.5, 2.5, 3.5]), 2.5)

    def test_empty_list(self):
        """Test mean calculation with an empty list."""
        self.assertIsNone(calculate_mean([]))

    def test_invalid_input_not_a_list(self):
        """Test that a TypeError is raised for non-list input."""
        with self.assertRaises(TypeError):
            calculate_mean("not a list")

    def test_invalid_input_non_numeric_elements(self):
        """Test that a TypeError is raised for non-numeric elements in the list."""
        with self.assertRaises(TypeError):
            calculate_mean([1, 2, "three", 4])

    def test_allow_infinity(self):
        """Test mean calculation with a list containing positive infinity."""
        self.assertEqual(calculate_mean([float("inf"), 2, 3]), float("inf"))

    def test_allow_negative_infinity(self):
        """Test mean calculation with a list containing negative infinity."""
        self.assertEqual(calculate_mean([float("-inf"), 2, 3]), float("-inf"))

    def test_large_numbers(self):
        """Test mean calculation with very large numbers."""
        self.assertAlmostEqual(calculate_mean([1e9, 2e9, 3e9]), 2e9)

    def test_small_numbers(self):
        """Test mean calculation with very small numbers."""
        self.assertAlmostEqual(calculate_mean([1e-9, 2e-9, 3e-9]), 2e-9)

    def test_zeros(self):
        """Test mean calculation with a list of zeros."""
        self.assertEqual(calculate_mean([0, 0, 0, 0]), 0.0)


if __name__ == "__main__":
    unittest.main()
