#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A module containing tests for the count_words function in solutions/count_words.py

Module contents:
    TestCountWords: A class that contains tests for the count_words function.

Created on Sunday, 29th December, 2024.
@author: Gai Samuel
"""

import unittest

from solutions.count_words import count_words


class TestCountWords(unittest.TestCase):
    """Tests for count_words function"""

    def test_count_words(self):
        """Returns the correct word count for each word in the text"""
        self.assertEqual(
            count_words("My name is Gai"), {"my": 1, "name": 1, "is": 1, "gai": 1}
        )

    def test_count_words_with_an_empty_string(self):
        """Returns an empty dictionary for an empty string"""
        self.assertEqual(count_words(""), {})

    def test_count_words_with_punctuation(self):
        """Returns the correct word count for each word in the text with punctuation"""
        self.assertEqual(
            count_words("My name is Gai."), {"my": 1, "name": 1, "is": 1, "gai.": 1}
        )

    def test_count_words_with_uppercase(self):
        """Returns the correct word count for each word in the text with uppercase"""
        self.assertEqual(
            count_words("MY NAME IS GAI"), {"my": 1, "name": 1, "is": 1, "gai": 1}
        )

    def test_count_words_with_multiple_spaces(self):
        """Returns the correct word count for each word in the text with multiple spaces"""
        self.assertEqual(
            count_words("My  name  is  Gai"), {"my": 1, "name": 1, "is": 1, "gai": 1}
        )

    def test_count_words_differ_by_case(self):
        """counts words that are the same but differ by case as same word"""
        self.assertEqual(
            count_words("GAI is good. Gai likes to code"),
            {"gai": 2, "is": 1, "good.": 1, "likes": 1, "to": 1, "code": 1},
        )

    def test_count_words_with_numbers(self):
        """counts the number in the text as a word of it's own"""
        self.assertEqual(
            count_words("Gai is 24 years old"),
            {"gai": 1, "is": 1, "24": 1, "years": 1, "old": 1},
        )

    def test_count_words_with_special_characters(self):
        """counts words with special characters and the special characters as same word"""
        self.assertEqual(
            count_words("Hello, Gai! How are you?"),
            {"hello,": 1, "gai!": 1, "how": 1, "are": 1, "you?": 1},
        )

    def test_count_same_words_with_different_special_characters(self):
        """counts words that are the same but differ by special characters as different words"""
        self.assertEqual(
            count_words("Hello Gai! How are you, Gai?"),
            {"hello": 1, "gai!": 1, "how": 1, "are": 1, "you,": 1, "gai?": 1},
        )

    def test_count_words_invalid_input(self):
        """Raises an AttributeError for invalid input"""
        with self.assertRaises(AttributeError):
            count_words(2025)
