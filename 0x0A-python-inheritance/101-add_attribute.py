#!/usr/bin/python3
"""Add attributes to an object"""


def add_attribute(obj, name, value):
    """
    Function that adds a new attribute to an object

    Args:
        obj: Object
        name: Attribute name
        value (any): Attribute value

    Raises:
        TypeError: When attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
