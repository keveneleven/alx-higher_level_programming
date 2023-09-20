#!/usr/bin/python3
"""Define text file functions"""


def read_file(filename=""):
    """Reads a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
