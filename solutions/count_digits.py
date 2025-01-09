#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module to count the number of digits in a given number.

Module contents:
    - count_digits: Counts the number of digits in a given number.

Created on Wednesday, 1st January, 2025.
@author: Gai Samuel
"""


def count_digits(number: int | float | str | bool) -> int:
    """
    The count_digits function counts the number of digits in a given number.

    Parameters:
        number: an integer/string/ boolean or float number whose digits are to be counted.

    Returns:
        An integer representing the number of digits in the input number.
        Note that the negative sign is not counted as a digit.

    Raises:
        ValueError:
            If the input is empty.
            If the input is not an integer, float, or numeric string.
        TypeError:
            if there is an invalid input.

    Example:
    >>> count_digits(34)
    2
    >>> count_digits(-17)
    2
    >>> count_digits(0)
    1
    >>> count_digits(19.5)
    2
    >>> count_digits("24")
    2
    """
    # Check for empty input
    if number == "":
        raise ValueError("The input cannot be empty.")

    # Converts a boolean to an integer.
    if isinstance(number, bool):
        number = int(number)

    # converts a float to an integer.
    if isinstance(number, float):
        number = int(number)

    # Handles a string input but raises a ValueError if the string is not a number.
    if isinstance(number, str):
        try:
            number = int(number)
        except ValueError as exc:
            raise ValueError("Input must be a valid number.") from exc

    # Check for empty or invalid inputs
    if not isinstance(number, (int, float, str, bool)):
        raise TypeError("Input must be an integer, float, boolean or numeric string.")

    # Convert the number to a string and remove the negative sign if present.
    number_str = str(abs(int(number)))

    return len(number_str)
