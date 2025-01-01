#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for even_odd_checker function.
Contains intentionally buggy tests for debugging practice.

Test categories:
    - Standard cases: different integers
    - Edge cases: empty input, single numbers, large numbers
    - Defensive tests: wrong input types, assertions

Created on 2024-12-31
Author: Robel Mengsteab
"""

import unittest
from ..even_odd_checker import even_odd_checker  # type: ignore


class TestEvenOddChecker(unittest.TestCase):
    """Test the prime_checker function - contains buggy tests!"""

    # Standard test cases

    def test_negative_three(self):
        """It should return Odd"""
        self.assertEqual(even_odd_checker(-3), "Odd")

    def test_negative_two(self):
        """It should return Even"""
        self.assertEqual(even_odd_checker(-2), "Even")

    def test_negative_one(self):
        """It should return Odd"""
        self.assertEqual(even_odd_checker(-1), "Odd")

    def test_zero(self):
        """It should return Even"""
        self.assertEqual(even_odd_checker(0), "Even")

    def test_one(self):
        """It should return Odd"""
        self.assertEqual(even_odd_checker(1), "Odd")

    def test_two(self):
        """It should return Even"""
        self.assertEqual(even_odd_checker(2), "Even")

    def test_three(self):
        """It should return Odd"""
        self.assertEqual(even_odd_checker(3), "Odd")

    # Edge cases
    def test_large_positive_odds(self):
        """It should return Odd"""
        self.assertEqual(even_odd_checker(1000003457), "Odd")

    def test_large_positive_evens(self):
        """It should return Even"""
        self.assertEqual(even_odd_checker(1000003400), "Even")

    def test_large_negative_odds(self):
        """It should return odd"""
        self.assertEqual(even_odd_checker(-23456789), "Odd")

    def test_large_negative_evens(self):
        """It should return even"""
        self.assertEqual(even_odd_checker(-23469574390), "Even")

    def test_positive_whole_float(self):
        """It should return Even"""
        self.assertEqual(even_odd_checker(6.0), "Even")

    def test_negative_whole_float(self):
        """It should return Odd"""
        self.assertEqual(even_odd_checker(-99), "Odd")

    # Defensive tests
    def test_no_input(self):
        """It should raise ValueError No Input"""
        with self.assertRaises(ValueError):
            even_odd_checker(None)

    def test_string(self):
        """It should raise TypeError for String"""
        with self.assertRaises(TypeError):
            even_odd_checker("MIT")

    def test_floats(self):
        """It should raise AssertionError for Float"""
        with self.assertRaises(AssertionError):
            even_odd_checker(6.56)


if __name__ == "__main__":
    unittest.main()
