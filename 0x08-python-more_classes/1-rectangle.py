#!/usr/bin/python3
"""
Module defines a class Rectangle
"""


class Rectangle:
    """Representation of a triangle."""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height attribute."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
