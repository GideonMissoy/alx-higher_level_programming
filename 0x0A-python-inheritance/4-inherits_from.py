#!/usr/bin/python3
"""
Function returns True if the objeect is an instance of a class that
inherited from the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """True if is class, false otherwise"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
