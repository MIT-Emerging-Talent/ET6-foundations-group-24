#!/usr/bin/env python3
# -- coding: utf-8 --

"""
This module contains the implementation of the `find_maximum_minimum` function.
The `find_maximum_minimum` function finds the maximum and minimum values from a list of numbers.

The function returns a tuple where the first element is the maximum value
and the second element is the minimum value from the list of numbers.

Edge cases such as an empty list or invalid inputs are handled appropriately.

@author: Yonatan Y. Yifat
"""

from typing import List, Tuple


def find_maximum_minimum(numbers: List[float]) -> Tuple[float, float]:
    """
    Function to find the maximum and minimum from a list of numbers.

    Args:
        numbers (List[float]): A list of numerical values (integers or floats).

    Returns:
        Tuple[float, float]: A tuple containing the minimum and maximum values in the list.

    Raises:
        ValueError: If the list is empty or if the list contains non-numeric elements.

    Examples:
        >>> find_maximum_minimum([5, 10, 15, 20])
        (5, 20)
        >>> find_maximum_minimum([-5, -10, -15, -20])
        (-20, -5)
        >>> find_maximum_minimum([1.5, 2.5, 3.5, 4.5])
        (1.5, 4.5)
    """
    if not numbers:
        raise ValueError("The list is empty, cannot determine maximum and minimum.")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError(
            "The list must contain only numeric values (integers or floats)."
        )
    return min(numbers), max(numbers)
