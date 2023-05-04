#!/usr/bin/python3
"""
Function defines a function `add_new_attr` that adds a new attribute to an object.
"""


def add_new_attr(obj, attr, value):
    """Adds a new attribute to an object.
    Args:
    obj (object): The object to which the attribute is added.
    attr (str): The name of the attribute to add.
    value (object): The value of the attribute to add.

    Raises:
    TypeError: If the object does not have a `__setattr__` method."""
    if hasattr(obj, '__setattr__'):
    setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
