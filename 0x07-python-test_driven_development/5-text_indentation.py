#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    m = 0
    while m < len(text) and text[m] == ' ':
        m += 1

    while m < len(text):
        print(text[m], end="")
        if text[m] == "\n" or text[m] in ".?:":
            if text[m] in ".?:":
                print("\n")
            m += 1
            while m < len(text) and text[m] == ' ':
                m += 1
            continue
        m += 1
