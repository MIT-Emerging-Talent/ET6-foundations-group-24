#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Name: intersection_of_two

Description: This module provides a function to find the intersection of two lists.
and returns a new list containing the common items between them.

The module includes: the following function:
    - intersection_of_two(first_list, second_list): Returns a new list with the intersection

Author: Linah Khayri
Date Created: 30-12-2024
"""


def intersection_of_two(first_list: list, second_list: list) -> list:
    """
    This function takes two lists and returns a list containing the intersection of them.
    The intersection includes only the items that are present in both
    first_list and second_list. The items in the intersection are returned only once,
    even if they appear multiple times in the input lists. The input lists
    can contain any type of items that are allowed in a list (e.g., integers,
    strings, floats, special characters, etc.)


    Parameters:
        first_list (list): The first list of items
        second_list (list): The second list of items

    Returns:
        intersection_list (list): A list containing the items that are common to both
            first_list and second_list and will not contain duplicate items.

    Raises:
        AssertionError: if first_list is not a list
        AssertionError: if second_list is not a list
        AssertionError: if any of the lists are empty

    >>> intersection_of_two([1, 2, 3, 4],[3, 4, 5, 6])
    [3, 4]
    >>> intersection_of_two(['a', 'cat', 'ABC', 'dog'],['c', 'abc', 'cat'])
    ['cat']
    >>> intersection_of_two(['$', '&', '@'],['$', '&', '@'])
    ['$', '&', '@']
    >>> intersection_of_two(['1', 3, 'girl'],['a', 4, 3, '1', 'boy'])
    ['1', 3]

    """
    assert isinstance(first_list, list), "first_list must be a list"
    assert isinstance(second_list, list), "second_list must be a list"
    assert len(first_list) > 0, "first_list can't be empty"
    assert len(second_list) > 0, "second_list can't be empty"

    intersection_list = []
    # Loop through each item in the first list
    for item in first_list:
        # Check if the item is in the second list and not already in the intersection
        if item in second_list and item not in intersection_list:
            intersection_list.append(item)

    return intersection_list
