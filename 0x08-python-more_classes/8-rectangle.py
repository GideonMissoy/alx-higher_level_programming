#!/usr/bin/python3
"""
This module defines a Rectangle class that represents a 2D rectangle.
"""


class Rectangle:
    """
    A rectangle class that defines a rectangle by its width and height.
    """

    # Class variables
    number_of_instances = 0  # Tracks the number of rectangle instances
    print_symbol = "#"       # Character used to represent the rectangle

    # Static method to compare areas of two rectangles
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the areas of two rectangles and returns the one with the
        larger area. If both have the same area, rect_1 is returned.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with the given width and height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # Getter and setter for the width property
    @property
    def width(self):
        """
        Getter for the private instance attribute width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the private instance attribute width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Getter and setter for the height property
    @property
    def height(self):
        """
        Getter for the private instance attribute height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the private instance attribute height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        if self.__width and self.__height:
            return 2 * (self.__width + self.__height)
        else:
            return 0

    def __str__(self):
        """
        Returns a string representation of the rectangle, using the character
        defined by print_symbol.
        """
        if self.__width and self.__height:
            return '\n'.join([str(self.print_symbol) * self.__width
                             for i in range(self.__height)])
        else:
            return ""

    def __repr__(self):
        """
        Returns a string representation of the rectangle in the format:
        'Rectangle(width, height)'
        """
        return f"Rectangle({self.__width}, {self.__height})"
