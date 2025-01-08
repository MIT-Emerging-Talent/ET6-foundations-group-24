#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A module that counts the number of times a word appears in a text.

Module contents:
    count_words: A function that counts the number of times a word appears in a text.

Created on Sunday, 29th December, 2024.
@author: Gai Samuel
"""


def count_words(text: str) -> dict:
    """A function that counts the number of times a word appears in a text.

    Parameters:
        text: A string of text.

    Returns:
        A dictionary of  the words in the text and the number of times they appear.

    Raises:
        AttributeError: If the text is not a string.

    Examples:
    >>> count_words("That is a good book")
    {'that': 1, 'is': 1, 'a': 1, 'good': 1, 'book': 1}

    >>> count_words("Coding is fun.")
    {'coding': 1, 'is': 1, 'fun.': 1}

    """
    # checks if the text is a string.
    if not isinstance(text, str):
        raise AttributeError("The text must be a string.")

    normalized_text = text.lower()  # converts the text to lowercase.
    words = normalized_text.split()  # splits the text into words of their own.

    words_count = {}
    for word in words:  # iterates through the separated words of the text.
        words_count[word] = (
            words_count.get(word, 0) + 1
        )  # counts the number of times a word appears in the text.

    return words_count
