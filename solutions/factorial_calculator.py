#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Name: factorial_calculator

Description: This module provides a function to calculate the factorial of a given number.

The module includes: the following function:
    - factorial_calculator(num): Returns the factorial of the input number num.

Author: Linah Khayri
Date Created: 29-12-2024
"""


def factorial_calculator(num: int | float) -> int:
    """
    This function calculates the factorial of a non-negative integer or whole float.

    The factorial of a non-negative integer n is the product of all positive integers
    less than or equal to num until we reach one.
    For example, the factorial of num! = num * (num-1) * ... * 1.
    Also 0 and 1 are special cases when it comes to calculating the factorial
    as their factorial is 1

    Parameters:

        num : int or float
        A non-negative integer or whole float whose factorial is to be computed.
        Whole floats are floats without a fractional part, such as 1.0 or 5.0.

    Returns:

        int: The factorial of the input number.

    Raises:AssertionError

        If num is a negative number, as factorial is not defined for negative numbers.

        If num is not an integer or a whole float (e.g., if it is a string,a non-whole float etc..).

    >>> factorial_calculator(0)
    1
    >>> factorial_calculator(1)
    1
    >>> factorial_calculator(5)
    120
    >>> factorial_calculator(4.0)
    24
    """
    # Check when the input is a float
    if isinstance(num, float):
        assert num.is_integer(), "Only proceed if the float is a whole number"
        num = int(num)  # Convert the whole float to an integer

    # Assert that num is an integer and non-negative
    assert isinstance(num, int), "Input must be an integer."
    assert num >= 0, "Input must be a non-negative integer."

    # Base case for recursion: factorial of 0 or 1 is 1
    if num == 0:  # Base case 1
        return 1  # turn-around 1

    if num == 1:  # Base case 2
        return 1  # turn-around 2

    # Recursive case: factorial_calculator(num) = num * factorial_calculator(num-1)
    # breaking-down num | Build-up by multiplying
    return num * factorial_calculator(num - 1)
