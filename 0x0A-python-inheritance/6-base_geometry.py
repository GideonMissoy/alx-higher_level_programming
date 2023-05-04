#!/usr/bin/python3
"""
class BaseGeometry with Public instance method: def area(self)
that raises an Exception with the message area() is not implemented
"""


class BaseGeometry:
    """A base class for geometry objects."""

    def area(self):
        """Raises an exception error"""
        raise Exception("area() is not implemented")
