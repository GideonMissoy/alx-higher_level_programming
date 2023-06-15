#!/usr/bin/python3
"""
Adds new attribute to object
"""


def add_attribute(obj, attr, value):
    """Attribute to add"""
    if not hasattr(obj, '__setattr__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

