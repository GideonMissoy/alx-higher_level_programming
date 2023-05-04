#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A base class for geometry objects."""
    def __init__(self, width, height):
        """init of rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return string rep rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
