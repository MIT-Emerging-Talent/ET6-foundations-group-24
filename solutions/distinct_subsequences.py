#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the number of distinct subsequences of one
string (t) in another string (s).
(LeetCode problem copied from
https://leetcode.com/problems/distinct-subsequences/)

Module contents:
    - count_distinct_subsequences: Computes the number of
    distinct subsequences of t in s using recursion with memoization.
    - _count_subsequences_recursive: A helper function to compute subsequences
    using recursion and memoization.

Dependencies:
    - functools: Used for the `cache` decorator for memoization.

Notes:
    - Implements a recursive approach with memoization to
    avoid recalculating overlapping subproblems.
    - Time complexity: O(len(s) * len(t)).
    - Space complexity: O(len(s) * len(t)).

Created on 26 12 2024
@author: Mohamed-Elnageeb
"""

import sys
from functools import cache  # Importing cache for memoization

sys.setrecursionlimit(10**6)  # Increase the limit to support deep recursion


def count_distinct_subsequences(s: str, t: str) -> int:
    """
    Computes the number of distinct subsequences of string t in string s.

    This function uses a recursive approach with memoization to efficiently
    calculate the number of ways string t can appear as a subsequence in s.

    Time Complexity:
        O(len(s) * len(t)): Each subproblem is solved once due to memoization.

    Space Complexity:
        O(len(s) * len(t)): Memoization table stores intermediate results.

    Parameters:
        s: str
            The source string in which to find subsequences.
        t: str
            The target string to match as a subsequence.

    Returns:
        int: The number of distinct subsequences of t in s.

    Raises:
        AssertionError: If the inputs are not strings.

    Examples:
    >>> count_distinct_subsequences("rabbbit", "rabbit")
    3

    >>> count_distinct_subsequences("abc", "abc")
    1

    >>> count_distinct_subsequences("abc", "def")
    0

    >>> count_distinct_subsequences("aaa", "aa")
    3
    """
    # Validate input
    assert isinstance(s, str), "Input s must be a string."
    assert isinstance(t, str), "Input t must be a string."

    @cache
    def _count_subsequences_recursive(s_index: int, t_index: int) -> int:
        """
        A helper function to recursively compute the number of subsequences
        with memoization.

        This function calculates how many distinct ways
        the substring t[t_index:] can appear as a subsequence
        in the substring `s[s_index:]`.

        Parameters:
            s_index: int
                Current index in string s.
            t_index: int
                Current index in string t.

        Returns:
            int: The number of ways t[t_index:] can appear
            as a subsequence in s[s_index:].

        Explanation of Recursion:
            - Base Case 1: If t_index == len(t),all characters of t
            have been matched,so return 1.
            - Base Case 2: If `s_index == len(s)`, the end of s is reached
            without matching all of t, so return 0.
            - Recursive Steps:
                - Exclude the current character of s
                (`_count_subsequences_recursive(s_index + 1, t_index)`).
                - Include the current character of s if it matches t[t_index]
                  (`_count_subsequences_recursive(s_index + 1, t_index + 1)`).

        """

        # All characters of t are matched, so increment the count
        if t_index == len(t):
            return 1
        # Reached the end of s without matching all characters of t
        if s_index == len(s):
            return 0

        # Exclude the current character of s and continue
        result = _count_subsequences_recursive(s_index + 1, t_index)

        # Include the current character of s in  if it matches t[t_index]
        if s[s_index] == t[t_index]:
            result += _count_subsequences_recursive(s_index + 1, t_index + 1)

        return result

    # Start the recursion from the beginning of both strings
    return _count_subsequences_recursive(0, 0)
