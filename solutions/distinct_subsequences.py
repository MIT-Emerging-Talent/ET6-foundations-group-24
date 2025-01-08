#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the number of distinct subsequences of one
string (target_str) in another string (source_str).
(LeetCode problem copied from
https://leetcode.com/problems/distinct-subsequences/)

Module contents:
    - distinct_subsequences: Computes the number of
    distinct subsequences of target_str in source_str.
    - _count_subsequences_recursive: A helper function to compute subsequences.

Dependencies:
    - functools: Used for the `cache` decorator.

Created on 26 12 2024
@author: Mohamed-Elnageeb
"""

import sys
from functools import cache

sys.setrecursionlimit(10**6)  # Increase the limit to support deep recursion


def distinct_subsequences(source_str: str, target_str: str) -> int:
    """
    Computes the number of distinct subsequences of string target_str
    in string source_str.

    This function calculates the number of ways string target_str
    can appear as a subsequence in source_str.

    Parameters:
        source_str: str
            The source string in which to find subsequences.
        target_str: str
            The target string to match as a subsequence.

    Returns:
        int: The number of distinct subsequences of target_str in source_str.

    Raises:
        TypeError: If the inputs are not strings.

    Examples:
    >>> distinct_subsequences("rabbbit", "rabbit")
    3

    >>> distinct_subsequences("abc", "abc")
    1

    >>> distinct_subsequences("abc", "def")
    0

    >>> distinct_subsequences("aaa", "aa")
    3
    """
    # Validate input
    if not isinstance(source_str, str):
        raise TypeError("Input source_str must be a string.")
    if not isinstance(target_str, str):
        raise TypeError("Input target_str must be a string.")

    @cache
    def _count_subsequences_recursive(source_idx: int, target_idx: int) -> int:
        """
        A helper function to compute the number of subsequences.

        This function calculates how many distinct ways
        the substring target_str[target_idx:] can appear as a subsequence
        in the substring source_str[source_idx:].

        Parameters:
            source_idx: int
                Current index in string source_str.
            target_idx: int
                Current index in string target_str.

        Returns:
            int: The number of ways target_str[target_idx:] can appear
            as a subsequence in source_str[source_idx:].
        """
        # Base case: All characters of target_str are matched
        if target_idx == len(target_str):
            return 1
        # Base case: End of source_str reached without matching all
        # characters of target_str
        if source_idx == len(source_str):
            return 0

        # Recursive case: Exclude the current character of source_str
        result = _count_subsequences_recursive(source_idx + 1, target_idx)

        # Recursive case: Include the current character of source_str if it
        # matches target_str[target_idx]
        if source_str[source_idx] == target_str[target_idx]:
            result += _count_subsequences_recursive(source_idx + 1, target_idx + 1)

        return result

    # Start the recursion from the beginning of both strings
    return _count_subsequences_recursive(0, 0)
