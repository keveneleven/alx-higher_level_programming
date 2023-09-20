#!/usr/bin/python3
"""Define text file functions"""


def write_file(filename="", text=""):
    """
    Write a string to file

    Args:
        filename (str): Name of filename
        text (str): Text to write
    Returns:
        Number of characters written
    """
    n_lines = 0
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
