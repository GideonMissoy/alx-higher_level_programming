#!/usr/bin/python3
"""
Contains the class BaseGeometry that raises an Exception.
"""


class BaseGeometry():
    """A class with public attribute area. """
	
    def area(self):
        """Raises an exception."""
        raise Exception("area() is not implemented")
