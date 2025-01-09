#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting binary numbers to decimal.

Module contents:
    - binary_to_decimal: converts binary numbers to decimal.

Created on 29/12/2024
@author: Khusro Sakhi
"""


def binary_to_decimal(binary_str: str) -> int:
    """
    Converts a binary number represented as a string into its decimal equivalent.

    Parameters:
        binary_str: A string representing the binary number (e.g., '1010')

    Returns:
        The decimal equivalent of the binary number as an integer

    Raises:
        TypeError: If the input is not a string or None.
        ValueError: If the input contains non-binary characters.

    >>> binary_to_decimal ("1010")
    10

    >>> binary_to_decimal ("1")
    1

    >>> binary_to_decimal ("100")
    4
    """

    if not isinstance(binary_str, str):
        raise TypeError("Entered value is not a string.")
    if not binary_str:
        raise ValueError("Input binary string cannot be empty.")
    if not all(bit in "01" for bit in binary_str):
        raise ValueError("Entered string contains non-binary characters.")

    decimal = 0
    length = len(binary_str)
    for i, bit in enumerate(binary_str):
        bit_value = int(bit)

        decimal += bit_value * (2 ** (length - i - 1))
    return decimal
