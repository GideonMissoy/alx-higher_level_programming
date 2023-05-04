#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square shape."""
    def __init__(self, size):
        """Initializes a new Square object with the given size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Computes and returns the area of the Square object."""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the Square object"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
