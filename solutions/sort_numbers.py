"""
A module for sorting a list of numbers.

Module contents: sorted list of numbers

Created on 2024-12-30

@author: Viktoriya Haiduk
"""


def sort_numbers(numbers: list) -> list:
    """
    Sorts a list of numbers.

    Parameters:
        numbers (list): A list of numbers to be sorted.
            - May contain integers or floats.
            - Must not contain non-numeric values.

    Returns -> list: Sorted list of numbers in ascending order.

    Raises: ValueError if the list is empty or contains non-numeric values.

    Examples:
        >>> sort_numbers([3, 1, 2])
        [1, 2, 3]
        >>> sort_numbers([4.5, 15.4, 6, 7, 2])
        [2, 4.5, 6, 7, 15.4]
        >>> sort_numbers([3.14159, 1.618, 2.718])
        [1.618, 2.718, 3.14159]
    """
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")

    if not numbers:
        raise ValueError("The list is empty. Please provide numbers to sort.")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("The list contains non-numeric values.")

    return sorted(numbers)
