#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer nad boolean) for
    JSON serialization of an object.

    Args:
        obj (any): Object
    """
    return obj.__dict__
