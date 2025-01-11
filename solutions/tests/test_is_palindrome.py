#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Testing module for is_palindrome function
Contains tests for checking proper work of is_palindrome function

Created on 2024-12-30
Author: Viktoriya Haiduk
"""

import unittest

from solutions.is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """
    Unit test class for the is_palindrome function.
    This class contains various test cases to validate the correctness
    and robustness of the palindrome checking function.
    """

    def test_palindrome_level(self):
        """
        Test case to check if the string 'level' is correctly identified as a palindrome.
        """
        self.assertTrue(is_palindrome("level"))

    def test_palindrome_radar(self):
        """
        Test case to check if the string 'radar' is correctly identified as a palindrome.
        """
        self.assertTrue(is_palindrome("radar"))

    def test_palindrome_empty(self):
        """
        Test case to check if an empty string is correctly identified as a palindrome.
        """
        self.assertTrue(is_palindrome(""))

    def test_not_palindrome_hello(self):
        """
        Test case to check if the string 'hello' is correctly identified as not a palindrome.
        """
        self.assertFalse(is_palindrome("hello"))

    def test_not_palindrome_world(self):
        """
        Test case to check if the string 'world' is correctly identified as not a palindrome.
        """
        self.assertFalse(is_palindrome("world"))

    def test_single_character_a(self):
        """
        Test case to check if a single character 'a' is correctly identified as a palindrome.
        """
        self.assertTrue(is_palindrome("a"))

    def test_single_character_z(self):
        """
        Test case to check if a single character 'z' is correctly identified as a palindrome.
        """
        self.assertTrue(is_palindrome("z"))

    def test_case_insensitive_level(self):
        """
        Test case to check if the function is case insensitive and identifies 'Level' as a palindrome.
        """
        self.assertTrue(is_palindrome("Level"))

    def test_case_insensitive_python(self):
        """
        Test case to check if the function correctly identifies 'Python' as not a palindrome,
        even with different cases.
        """
        self.assertFalse(is_palindrome("Python"))

    def test_whitespace_palindrome(self):
        """
        Test case to check if a palindrome with spaces is correctly identified.
        """
        processed_string = "A man a plan a canal Panama".replace(" ", "").lower()
        self.assertTrue(is_palindrome(processed_string))

    def test_whitespace_not_palindrome(self):
        """
        Test case to check if a string with spaces that is not a palindrome is correctly identified.
        """
        self.assertFalse(is_palindrome("Not a palindrome"))


if __name__ == "__main__":
    unittest.main()
