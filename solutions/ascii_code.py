#!/usr/bin/env python3
# --#coding: utf-8 --
"""
Description: This file contains the ASCII code conversion functionality.

Write a function that takes a string as input and returns a list of ASCII
codes of the characters in the input string.

date : 2024-12-31
@Author : Zeinab Mohmmed

"""


def ascii_code(text: str) -> list:
    """
    Convert a string to a list of ASCII codes.

    parameters:
    text: a string of characters

    Returns:
    a list of integers, where each integer is the ASCII code of the character
    at the corresponding index in the input string

    Raises:
    TypeError: if the input is not a string
    e.g. ascii_code(123)

    Example:
    >>> ascii_code('abc')
    [97, 98, 99]

    >>> ascii_code('!')
    [33]

    >>> ascii_code('')
    []

    >>> ascii_code(' ')
    [32]

    >>> ascii_code('0')
    [48]
    """
    # Check if the input is not a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    # Check if the input is an empty string
    if text == "":
        return []
    # Convert the string to a list of ASCII codes
    ascii_values = []
    # Iterate over the characters in the input string
    for i in text:
        ascii_values.append(ord(i))
    return ascii_values
