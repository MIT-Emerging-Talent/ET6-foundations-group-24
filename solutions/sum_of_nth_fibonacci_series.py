"""
This module contains the implementation of the `sum_of_nth_fibonacci_series` function.

The `sum_of_nth_fibonacci_series` function computes the sum of the first n Fibonacci numbers,
where n is a non-negative integer. The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

This module is designed to be efficient and handles edge cases such as n = 0 or negative inputs.

@author: Yonatan Y. Yifat
"""


def sum_of_nth_fibonacci_series(n: int) -> int:
    """
    Calculate the sum of the first n numbers in the Fibonacci series.

    The Fibonacci series is defined as:
    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

    Parameters:
    n (int): The number of terms in the Fibonacci series to sum.

    Returns:
    int: The sum of the first n numbers in the Fibonacci series.

    Raises:
    TypeError: If the input is not an integer.
    ValueError: If the input is a negative integer.

    Example:
    >>> sum_of_nth_fibonacci_series(3)
    2
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Initialize the first two Fibonacci numbers and the sum
    a, b = 0, 1
    total_sum = a

    for _ in range(1, n):
        total_sum += b
        a, b = b, a + b

    return total_sum
