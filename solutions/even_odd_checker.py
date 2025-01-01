#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking whether a number is even or odd.

Module contents:
    - even_odd_checker: checks if a given number is even or odd.

Created on 2024-12-31
Author: Robel Mengsteab
"""

def even_odd_checker(n: int) -> str:
    """Checks if a number is even or odd.
    
    Determines if the input number is even or odd and validates the input.
    
    Parameters:
        n: int, the number to check.
        
    Returns -> str: "Even" if the number is even, "Odd" if the number is odd.
    
    Raises:
        AssertionError: if input is not an integer or a whole number float.
        ValueError: if no input is provided
        TypeError: if input is a string or invalid type.
    
    Examples:
        >>> even_odd_checker(2)
        'Even'
        >>> even_odd_checker(3)
        'Odd'
        >>> even_odd_checker(2.0)
        'Even'
        >>> even_odd_checker(-5.0)
        'Odd'
        >>> even_odd_checker(-6)
        'Even'
        >>> even_odd_checker(-1)
        'Odd'
    """
    
    # Checks if there is no value given
    if n is None:
        raise ValueError("Input cannot be None")
    # Raises a TypeError if the input is a String
    if isinstance(n, str):
        raise TypeError("Input cannot be a string")
    
    # Checks if the given input is an integer or a whole float
    assert isinstance(n, (int, float)), "Input must be an integer or a whole float"
    
    # Check if float is not a whole number
    if n != int(n):
        raise AssertionError("Input must be an integer or a whole float")
    
    # Convert to integer if it's a whole number float
    n = int(n)
    
    # Check if the number is even or odd
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
