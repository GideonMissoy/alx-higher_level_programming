#!/usr/bin/python3
"""
class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """Rectangle information: width, height"""

    def __init__(self, width=0, height=0):
        """Initialize a new instance of the Rectangle class."""

        self.height = height
        self.width = width

    def __del__(self):
        """Deletes an instance of the Rectangle class."""

        print("Bye rectangle...")

    @property
    def width(self):
        """Return the width of the rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the width of the rectangle."""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle."""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the height of the rectangle."""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""

        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle."""

        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the rectangle with the character #."""

        Estring = ""
        if self.__width != 0 and self.__height != 0:
            Estring += "\n".join("#" * self.__width
                               for i in range(self.__height))
        return Estring

    def __repr__(self):
        """Return a string representation of the rectangle."""

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
