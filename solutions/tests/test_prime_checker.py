#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for prime_checker function.
Contains intentionally buggy tests for debugging practice.

Test categories:
    - Standard cases: different positive numbers
    - Edge cases: zero, large number, single digit, two digit,whole floats
    - Defensive tests: wrong input types, assertions

Created on 2024-12-31
Author: Robel Mengsteab
"""

import unittest
from ..prime_checker import prime_checker


class TestPrimeChecker(unittest.TestCase):
    """Test the prime_checker function - contains buggy tests!"""

    # Standard test cases
    def test_two(self):
        """It should return True"""
        self.assertEqual(prime_checker(2), True)

    def test_number_three(self):
        """It should return True"""
        self.assertEqual(prime_checker(3), True)

    def test_number_four(self):
        """It should return False"""
        self.assertEqual(prime_checker(4), False)

    def test_number_five(self):
        """It should return True"""
        self.assertEqual(prime_checker(5), True)

    def test_number_six(self):
        """It should return False"""
        self.assertEqual(prime_checker(6), False)

    def test_number_seven(self):
        """It should return True"""
        self.assertEqual(prime_checker(7), True)

    def test_number_eight(self):
        """It should return False"""
        self.assertEqual(prime_checker(8), False)

    def test_number_nine(self):
        """It should return False"""
        self.assertEqual(prime_checker(9), False)
# Edge cases
    def test_zero(self):
        """It should return False"""
        self.assertEqual(prime_checker(0), False)

    def test_number_one(self):
        """It should return False"""
        self.assertEqual(prime_checker(1), False)

    def test_large_number(self):
        """It should return"""
        self.assertEqual(prime_checker(100019), True)

    def test_single_digit(self):
        """It should return True or False based on the given number"""
        self.assertEqual(prime_checker(5), True)

    def test_two_digits(self):
        """It should return True or False based on the given number"""
        self.assertEqual(prime_checker(23), True)
        
    def test_whole_floats(self):
        """It should return True"""
        self.assertEqual(prime_checker(7.0), True)
            
# Defensive tests
    def test_no_input(self):
        """It should raise AssertionError for No input"""
        with self.assertRaises(ValueError):
            prime_checker(None)
    
    def test_negatives(self):
        """It should raise AssertionError for Negatives"""
        with self.assertRaises(ValueError):
            prime_checker(-1)
    def test_string(self):
        """It should raise AssertionError for String values"""
        with self.assertRaises(TypeError):
            prime_checker("hello")
    def test_fractional_floats(self):
        """It should raise AssertionError for fractional Float"""
        with self.assertRaises(AssertionError):
            prime_checker(5.56)

if __name__ == "__main__":
    unittest.main()
