#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_leap function.

Test categories:
    - Standard cases: Common leap and non-leap years
    - Edge cases: Smallest leap year, non-leap years close to leap years
    - Defensive tests: Handling of invalid inputs (e.g., non-integer, negative values)

Created on 29/12/2024

@author: Khusro Sakhi
"""

import unittest

from ..is_leap_year import is_leap_year


class TestLeapYear(unittest.TestCase):
    """Test suite for the is_leap function - contains buggy tests!"""

    # Standard test cases
    def test_leap_year_2000(self):
        """It should return True for the year 2000 (divisible by 400)"""
        self.assertTrue(is_leap_year(2000))

    def test_non_leap_year_1990(self):
        """It should return False for the year 1990 (not divisible by 4)"""
        self.assertFalse(is_leap_year(1990))

    def test_non_leap_year_2100(self):
        """It should return False for the year 2100 (divisible by 100 but not by 400)"""
        self.assertFalse(is_leap_year(2100))

    def test_leap_year_2004(self):
        """It should return True for the year 2004 (divisible by 4 but not by 100)"""
        self.assertTrue(is_leap_year(2004))

    # Edge cases
    def test_leap_year_4(self):
        """It should return True for the year 4 (the smallest leap year)"""
        self.assertTrue(is_leap_year(4))

    def test_non_leap_year_1(self):
        """It should return False for the year 1 (not divisible by 4)"""
        self.assertFalse(is_leap_year(1))

    def test_non_leap_year_100(self):
        """It should return False for the year 100 (divisible by 100 but not by 400)"""
        self.assertFalse(is_leap_year(100))

    # Defensive tests
    def test_string_input(self):
        """It should raise TypeError for a string input"""
        with self.assertRaises(TypeError):
            is_leap_year("2000")

    def test_negative_year(self):
        """It should raise ValueError for a negative year"""
        with self.assertRaises(ValueError):
            is_leap_year(-4)

    def test_none_input(self):
        """It should raise TypeError for None input"""
        with self.assertRaises(TypeError):
            is_leap_year(None)

    def test_zero_input(self):
        """It should raise ValueError for 0 input"""
        with self.assertRaises(ValueError):
            is_leap_year(0)

    def test_float_input(self):
        """It should raise TypeError for a float input"""
        with self.assertRaises(TypeError):
            is_leap_year(4.5)


if __name__ == "__main__":
    unittest.main()
