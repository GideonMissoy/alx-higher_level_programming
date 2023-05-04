#!/usr/bin/python3
"""
Function adds a new attribute to an object
"""


def add_new_attr(obj, attr, value):
    """Attribute to add"""
    if hasattr(obj, '__setattr__'):
    setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
