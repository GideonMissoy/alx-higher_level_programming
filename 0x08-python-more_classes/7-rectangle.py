#!/usr/bin/python3
"""
Module contains class Rectangle that defines a rectangle.
"""


class Rectangle:
    """representation of a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def set_print_symbol(cls, symbol):
        """sets printing symbol."""
        cls.print_symbol = symbol

    def __init__(self, width=0, height=0):
        """initializes the rectangle."""
        self.height = height
        self.width = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints a str when an instance has been deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """getter for the private instance attributre width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter attribute for the width instance."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter attribute for the height instance."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 and self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """prints the rectangle instance with the character '#'"""
        Estring = ""
        if self.__width != 0 and self.__height != 0:
            Estring += "\n".join(print_symbol * self.__width
                                 for i in range(self.__height))

    def __repr__(self):
        """returns a string rep of the rect for reproduction."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
