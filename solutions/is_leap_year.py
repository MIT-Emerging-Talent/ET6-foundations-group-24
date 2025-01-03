#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for determining whether the given year is leap year or not

Module contents:
    - is_leap: determines whether the given year is leap year or not.

Created on 29/12/2024
@author: Khusro Sakhi
"""


def is_leap_year(year: int) -> bool:
    """Determines if the given year is a leap year.

    Parameters:
        year (int): The year to test.

    Returns:
        bool: True if the year is a leap year, False otherwise.

     Raises:
        AssertionError: If the input is a string.
        AssertionError: If the input is a negative year.
        AssertionError: If the input is None.
        AssertionError: If the input is a float.

    >>> is_leap(2000)
    True

    >>> is_leap(1990)
    False

    >>> is_leap(2100)
    False

    >>> is_leap(2004)
    True
    """
    assert isinstance(year, int), "entered year is not an integer"
    assert year > 0, "year is less than 0"

    # A leap year is divisible by 4, but not by 100 unless also divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
