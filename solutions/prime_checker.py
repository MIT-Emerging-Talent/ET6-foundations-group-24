#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking prime numbers.

Module contents:
    - prime_checker: checks if a given number is prime or not.

Created on 2024-12-31
Author: Robel Mengsteab
"""

def prime_checker(n: int) -> bool:
    """Checks if a number is prime.
    
    A prime number is greater than 1 and divisible only by 1 and itself.
    
        
    Parameters:
        n: int, the number to greater than one
        
    Returns -> bool: True if n is prime, False otherwise
    
    Raises:
        AssertionError: if input is not an integer
        ValueError: If no input is provided.
    
    Examples:
        >>> prime_checker(2)
        True
        >>> prime_checker(1)
        False
        >>> prime_checker(13)
        True
        >>> prime_checker(6)
        False
    """
    
    # Checks if there is no value given
    if n is None:
        raise ValueError("Input cannot be None")
    # Raises a TypeError if the input is a String
    if n is str:
        raise TypeError("Input cannot be a String")
    
    # Raises an error if the given number is negative
    if n < 0:
        raise ValueError("Input cannot be Negative")
    
    #Checks if the given input is integer or Float
    assert isinstance(n, (int, float)), "Input must be an integer or a Whole float"
    
    # Check if float is not a whole number
    if n != int(n):  
        raise AssertionError("Input must be a whole number float, not a fractional float")
    
    # Convert to integer if it's a whole number float
    n = int(n)  
    
    # Checks if the given number is less than or equal to one
    if n <= 1:
        return False
    
    # Checks whether the numbers greater than one are prime or not
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True
