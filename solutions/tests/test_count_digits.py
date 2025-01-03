#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module containing tests for the count_digits function.

created on Wednesday, 1st January, 2025.
@author: Gai Samuel
"""

import unittest

from ..count_digits import count_digits


class TestCountDigits(unittest.TestCase):
    """Tests for count_digits function"""

    def test_positive_integer(self):
        """It returns the number of digits in a positive integer."""
        self.assertEqual(count_digits(24), 2)

    def test_negative_integer(self):
        """It returns the number of digits in a negative integer."""
        self.assertEqual(count_digits(-2024), 4)

    def test_zero(self):
        """It returns 1 for zero since it has one digit."""
        self.assertEqual(count_digits(0), 1)

    def test_large_integer(self):
        """It returns the number of digits in a large integer"""
        self.assertEqual(count_digits(12345678910), 11)

    def test_float_input(self):
        """It converts float to an integer and then returns corresponding number of digits."""
        self.assertEqual(count_digits(45.9), 2)

    def test_string_input(self):
        """It returns the number of digits in a string."""
        self.assertEqual(count_digits("15"), 2)

    def test_empty_input(self):
        """It raises a value error for an empty input"""
        with self.assertRaises(ValueError):
            count_digits("")

    def test_invalid_string_input(self):
        """It raises a value error for an invalid string input"""
        with self.assertRaises(ValueError):
            count_digits("Gai")

    def test_invalid_input(self):
        """It raises a type error for an invalid input"""
        with self.assertRaises(TypeError):
            count_digits([1, 2, 3])
            count_digits(None)
            count_digits({1, 2, 3})
            count_digits(True)
            count_digits(False)
            count_digits({"name": "Gai"})
