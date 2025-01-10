"""
Test module for sort_numbers function.

Contains tests for testing sort_numbers function.

Created on 2024-12-30
Author: Viktoriya Haiduk
"""

import unittest

from solutions.sort_numbers import sort_numbers


class TestSortNumbers(unittest.TestCase):
    def test_sorted_numbers(self):
        self.assertEqual(sort_numbers([4, 1, 3, 2]), [1, 2, 3, 4])

    def test_floats(self):
        self.assertEqual(sort_numbers([4.5, 2.3, 1.7, 3.9]), [1.7, 2.3, 3.9, 4.5])

    def test_mixed_numbers(self):
        self.assertEqual(sort_numbers([4, 2.5, 3, 1.2]), [1.2, 2.5, 3, 4])

    def test_invalid_input(self):
        with self.assertRaises(ValueError) as context:
            sort_numbers(["a", None, 3])
        self.assertEqual(
            str(context.exception), "The list contains non-numeric values."
        )

    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            sort_numbers([])
        self.assertEqual(
            str(context.exception), "The list is empty. Please provide numbers to sort."
        )

    def test_negative_numbers(self):
        self.assertEqual(sort_numbers([-3, -1, -4, -2]), [-4, -3, -2, -1])


if __name__ == "__main__":
    unittest.main()
