#!/usr/bin/python3
"""
Contains class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square that inherits from Rectangle."""
    def __init__(self, size):
        """Initializes a square."""
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Prints square."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
