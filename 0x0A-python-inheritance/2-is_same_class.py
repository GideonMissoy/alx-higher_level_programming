#!/usr/bin/python3
"""
Function returns True if object is exactly an instance of specified class.
"""


def is_same_class(obj, a_class):
    """returns true if object is exactly an instance of specified class."""
    return (type(obj) == a_class)
