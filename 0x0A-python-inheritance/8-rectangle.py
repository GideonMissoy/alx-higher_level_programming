#!/usr/bin/python3
"""
Contains a class Rectangle that inherits from class BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle."""
    def __init__(self, width, height):
        """Initializes the rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
