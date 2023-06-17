#!/usr/bin/python3
"""
Function returns True if the object is an instance of a class that
inherited directly the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """Returns True if is an instance of class inherited."""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
