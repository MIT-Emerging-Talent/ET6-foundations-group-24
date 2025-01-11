#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to check if two strings are anagrams.

Date created: Dec 31, 2024
Author: @Abel Teka
"""


def is_anagram(string1: str, string2: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    Args:
        string1 (str): The first string to compare.
        string2 (str): The second string to compare.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    Raises:
        AttributeError: If either argument is not a string.

    Examples:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("hello", "world")
        False
        >>> is_anagram("evil", "vile")
        True
    """
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise AttributeError("Both inputs must be strings.")

    # Normalize strings: remove spaces, convert to lowercase, and sort characters
    normalized1 = "".join(sorted(string1.replace(" ", "").lower()))
    normalized2 = "".join(sorted(string2.replace(" ", "").lower()))

    return normalized1 == normalized2
