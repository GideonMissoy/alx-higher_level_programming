#!/usr/bin/python3
"""
Function returns true if: The object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """True if object is an instance, False otherwise"""
    return isinstance(obj, a_class)
