"""
Test cases for the `sum_of_nth_fibonacci_series` function.

This module contains unit tests for verifying the functionality of the
`sum_of_nth_fibonacci_series` function, which computes the sum of the
first n Fibonacci numbers.

@author: Yonatan Y. Yifat
"""

import unittest

from solutions.sum_of_nth_fibonacci_series import sum_of_nth_fibonacci_series


class TestSumOfNthFibonacciSeries(unittest.TestCase):
    """Test suite for the sum_of_nth_fibonacci_series function."""

    # Standard test cases (existing ones retained)
    def test_zero_terms(self):
        self.assertEqual(sum_of_nth_fibonacci_series(0), 0)

    def test_single_term(self):
        self.assertEqual(sum_of_nth_fibonacci_series(1), 0)

    def test_two_terms(self):
        self.assertEqual(sum_of_nth_fibonacci_series(2), 1)

    def test_large_input(self):
        self.assertEqual(sum_of_nth_fibonacci_series(10), 88)

    # Edge cases (existing and new ones)
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            sum_of_nth_fibonacci_series(-5)

    def test_invalid_type_string(self):
        """It should raise a TypeError for string input."""
        with self.assertRaises(TypeError):
            sum_of_nth_fibonacci_series("text")

    def test_invalid_type_none(self):
        """It should raise a TypeError for None input."""
        with self.assertRaises(TypeError):
            sum_of_nth_fibonacci_series(None)

    def test_invalid_type_float(self):
        """It should raise a TypeError for float input."""
        with self.assertRaises(TypeError):
            sum_of_nth_fibonacci_series(2.5)

    def test_invalid_type_list(self):
        """It should raise a TypeError for list input."""
        with self.assertRaises(TypeError):
            sum_of_nth_fibonacci_series([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
