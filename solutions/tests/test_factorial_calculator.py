#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for factorial_calculator function.
Contains comprehensive tests to ensure the correctness
of the factorial_calculator function.
is designed to work only for positive integers and whole floats,
which are transformed to integers before calculation

Test categories:
    - Standard cases: Positive integers
    - Edge cases: zero factorial, one factorial, whole floats, large integers
    - Defensive tests: negative inputs, non-whole floats, non-integer input

Created on 29-12-2024
Author: Linah Khayri
"""

import unittest

from ..factorial_calculator import factorial_calculator


class TestFactorialCalculator(unittest.TestCase):
    """Test suite for the factorial_calculator function that handle different cases"""

    # Standard Cases
    def test_factorial_2(self):
        """It should calculate the factorial of 2 as it's a positive integer"""
        self.assertEqual(factorial_calculator(2), 2)

    def test_factorial_3(self):
        """It should calculate the factorial of 3 as it's a positive integer"""
        self.assertEqual(factorial_calculator(3), 6)

    def test_factorial_4(self):
        """It should calculate the factorial of 4 as it's a positive integer"""
        self.assertEqual(factorial_calculator(4), 24)

    def test_factorial_5(self):
        """It should calculate the factorial of 5 as it's a positive integer"""
        self.assertEqual(factorial_calculator(5), 120)

    def test_factorial_6(self):
        """It should calculate the factorial of 6 as it's a positive integer"""
        self.assertEqual(factorial_calculator(6), 720)

    def test_factorial_8(self):
        """It should calculate the factorial of 8 as it's a positive integer"""
        self.assertEqual(factorial_calculator(8), 40320)

    def test_factorial_12(self):
        """It should calculate the factorial of 12 as it's a positive integer"""
        self.assertEqual(factorial_calculator(12), 479001600)

    # Edge cases
    def test_factorial_0(self):
        """Test for factorial of 0 (special case). Factorial of 0 is always 1 by definition."""
        self.assertEqual(factorial_calculator(0), 1)

    def test_factorial_1(self):
        """Test for factorial of 1 (special case). Factorial of 1 is always 1 by definition."""
        self.assertEqual(factorial_calculator(1), 1)

    def test_factorial_whole_float(self):
        """It should handle whole floats and return the factorial as an integer"""
        self.assertEqual(factorial_calculator(7.0), 5040)

    def test_factorial_large_integer(self):
        """It should handle large integers"""
        self.assertEqual(
            factorial_calculator(50),
            30414093201713378043612608166064768844377641568960512000000000000,
        )

    def test_factorial_large_whole_float(self):
        """It should handle large whole floats"""
        self.assertEqual(factorial_calculator(20.0), 2432902008176640000)

    # Defensive tests:
    def test_negative_factorial_calculator(self):
        """should raise an error if the input num is a negative number"""
        with self.assertRaises(AssertionError):
            factorial_calculator(-5)

    def test_fractional_float_factorial_calculator(self):
        """should raise an error if the input num is not a whole float"""
        with self.assertRaises(AssertionError):
            factorial_calculator(3.5)

    def test_non_numeric_factorial_calculator(self):
        """should raise an error if the input num is not a number"""
        with self.assertRaises(AssertionError):
            factorial_calculator("cat")
