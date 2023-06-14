#!/usr/bin/python3
"""
Function that returns the list of available attributes,
and methods of an object.
"""


def lookup(obj):
"""Returns list of available attributes and methods."""
return dir(obj)

