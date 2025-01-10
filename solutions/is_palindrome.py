#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for checking if a string is a palindrome.

Module contents: check if input string is palindrome.
Created on 2024-12-30
Author: Viktoriya Haiduk
"""


def is_palindrome(string: str) -> bool:
    """
    Checks if a string is a palindrome. Ignores spaces, capitalization, and special characters.

    Parameters:
        string (str): Input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> is_palindrome("level")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("No lemon, no melon")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("")
        True
        >>> is_palindrome("12321")
        True
        >>> is_palindrome("123 321")
        True
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")

    # Normalize the string: remove non-alphanumeric characters, convert to lowercase
    normalized = "".join(char.lower() for char in string if char.isalnum())
    # Check if the normalized string is equal to its reverse
    return normalized == normalized[::-1]
