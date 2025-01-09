#!/usr/bin/env python3
# --#coding: utf-8 --
"""
Description: This file contains the test cases for the sum_range function.

This module defines the sum_range function that calculates the sum of all
integers from start to end (inclusive). The function raises a TypeError if
start or end is not an integer.

date:2024-12-31
@ author: Zeinab Mommed
"""


def sum_range(start: int, end: int) -> int:
    """
    Calculate the sum of all integers from start to end (inclusive).
    parameters:
        start (int): The starting integer.
        end (int): The ending integer.
    Returns:
        int: The sum of all integers from start to end (inclusive).

    Raises:
        TypeError: If start or end is not an integer e.g. float, string.

    Example:

    >>>sum_range(1, 20)
    210

    >>>sum_range(-10, 10)
    0

    >>>sum_range(10, 1)
    55

    >>>sum_range(5, 5)
    5

    >>>sum_range(100, 10000)
    50005000
    """
    # Check if start and end are integers
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Both start and end must be integers.")
    # Ensure start is less than or equal to end
    if start > end:
        start, end = end, start
    # Calculate the sum of the range
    total = 0
    for number in range(start, end + 1):
        total += number
    return total
