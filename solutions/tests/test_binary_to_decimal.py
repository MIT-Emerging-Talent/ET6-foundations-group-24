#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for binary_to_decimal function.
Contains intentionally buggy tests for debugging practice.

Test categories:
  - Standard cases: Typical binary numbers with various lengths and values.
  - Edge cases: Binary strings with leading zeros, empty strings, or single digits.
  - Defensive tests: Tests for invalid input types (e.g., non-strings, floats, `None`)
    and assertions (e.g., strings containing non-binary characters).



Created on XX XX XX

@author: Khusro Sakhi
"""

import unittest

from ..binary_to_decimal import binary_to_decimal


class TestBinaryToDecimal(unittest.TestCase):
    """Test suite for the binary_to_decimal function."""

    # Standard test cases
    def test_binary_1010(self):
        """It should return 10 for the binary '1010'."""
        self.assertEqual(binary_to_decimal("1010"), 10)

    def test_binary_0(self):
        """It should return 0 for the binary '0'."""
        self.assertEqual(binary_to_decimal("0"), 0)

    def test_binary_1(self):
        """It should return 1 for the binary '1'."""
        self.assertEqual(binary_to_decimal("1"), 1)

    def test_binary_1111(self):
        """It should return 15 for the binary '1111'."""
        self.assertEqual(binary_to_decimal("1111"), 15)

    def test_binary_100000(self):
        """It should return 32 for the binary '100000'."""
        self.assertEqual(binary_to_decimal("100000"), 32)

    # Edge cases
    def test_empty_string(self):
        """It should raise a ValueError for an empty string."""
        with self.assertRaises(ValueError):
            binary_to_decimal("")

    def test_leading_zeros(self):
        """It should correctly handle binary strings with leading zeros."""
        self.assertEqual(binary_to_decimal("000101"), 5)

    # Large number test
    def test_large_binary_number(self):
        """It should correctly convert a very large binary number."""
        large_binary = "1" * 50  # A binary number with 50 ones (111...111)
        # Compute the expected decimal using Python's int function
        expected_decimal = int(large_binary, 2)
        self.assertEqual(binary_to_decimal(large_binary), expected_decimal)

    # Defensive tests
    def test_invalid_characters(self):
        """It should raise an AssertionError for non-binary characters."""
        with self.assertRaises(AssertionError):
            binary_to_decimal("10A01")

    def test_non_string_input(self):
        """It should raise an AssertionError for non-string input."""
        with self.assertRaises(AssertionError):
            binary_to_decimal(1010)

    def test_none_input(self):
        """It should raise an AssertionError for None input."""
        with self.assertRaises(AssertionError):
            binary_to_decimal(None)

    def test_float_input(self):
        """It should raise an AssertionError for a float input."""
        with self.assertRaises(AssertionError):
            binary_to_decimal(10.1)


if __name__ == "__main__":
    unittest.main()
