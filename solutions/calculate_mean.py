#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to calculate the mean (average) of a list of numbers.

Date created: Dec 30,2024
Author: @Abel Teka
"""

from typing import List, Optional


def calculate_mean(numbers: List[float]) -> Optional[float]:
    """
    Calculate the mean (average) of a list of numbers.

    Args:
        numbers (List[float]): A list of numbers (integers or floats).

    Returns:
        Optional[float]: The mean (average) of the numbers in the list.
            - Returns None if the list is empty.
            - Returns infinity if the sum of the list is infinite.

    Raises:
        TypeError: If `numbers` is not a list or contains non-numeric elements.

    Examples:
        >>> calculate_mean([1, 2, 3, 4, 5])
        3.0
        >>> calculate_mean([10, 20, 30])
        20.0
        >>> calculate_mean([])

        >>> calculate_mean([float('inf'), 1, 2])
        inf
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if any(not isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements in the list must be numbers.")

    if not numbers:
        return None

    return sum(numbers) / len(numbers)
