#!/usr/bin/env python3
# --#coding: utf-8 --

"""
DESCRIPTION: Tests for the ASCII code conversion functionality.

This module contains a test suite for the ASCII code conversion functionality.
Tests cover standard ASCII characters, whitespace characters, special characters,
numeric characters, and word inputs. It also includes tests for handling invalid
inputs such as empty strings, numbers, lists of numbers, and boolean values.

Date: 2024-12-31
Author: Zeinab Mohammed
"""

# Import the unittest module
import unittest

# Import the function to be tested
from solutions.ascii_code import ascii_code


# Define a test suite for the ASCII code conversion functionality:
class TestAsciiCode(unittest.TestCase):
    """Test suite for ASCII code conversion functionality."""

    def test_basic_capital_chars(self):
        """Test conversion of capital characters."""
        self.assertEqual(ascii_code("C"), [67])

    def test_small_chars(self):
        """Test conversion of small characters."""
        self.assertEqual(ascii_code("c"), [99])

    def test_edge_cases(self):
        """Test conversion of edge cases."""
        self.assertEqual(ascii_code("A"), [65])

    def test_special_chars(self):
        """Test conversion of special characters."""
        self.assertEqual(ascii_code("@"), [64])

    def test_numbers(self):
        """Test conversion of numeric characters."""
        self.assertEqual(ascii_code("0"), [48])

    def test_word_input(self):
        """Test handling of word inputs."""
        self.assertEqual(ascii_code("Hello"), [72, 101, 108, 108, 111])

    def test_whitespace(self):
        """Test conversion of whitespace characters."""
        self.assertEqual(ascii_code(" "), [32])  # space

    def test_empty_input(self):
        """Test handling of empty string input."""
        self.assertEqual(ascii_code(""), [])

    def test_None_input(self):
        """Test handling of None input."""
        with self.assertRaises(TypeError):
            ascii_code(None)

    def test_number_input(self):
        """Test handling of number input."""
        with self.assertRaises(TypeError):
            ascii_code(123)

    def test_boolean_input(self):
        """Test handling of boolean input."""
        with self.assertRaises(TypeError):
            ascii_code(True)

    def test_invalid_input(self):
        """Test handling of float input."""
        with self.assertRaises(TypeError):
            ascii_code(12.3)


# Run the test suite
if __name__ == "__main__":
    unittest.main()
