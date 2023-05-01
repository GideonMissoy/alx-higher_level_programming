#!/usr/bin/python3
"""
class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """Class that defines a rectangle"""

    # Public class attribute that keeps track of the number of instances
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializer method that sets the width and height of a new rectangle
        """

        self.width = width
        self.height = height

        # Increment the number of instances
        # every time a new Rectangle object is created
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        Destructor method that is called when a Rectangle object is deleted
        """

        print("Bye rectangle...")

        # Decrement the number of instances when a Rectangle object is deleted
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter method that returns the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter method that sets the width of the rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter method that returns the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter method that sets the height of the rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Method that calculates and returns the area of the rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Method that calculates and returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Method that returns a string representation of the rectangle"""

        Estring = ""

        if self.__width != 0 and self.__height != 0:
            Estring += "\n".join("#" * self.__width
                                    for i in range(self.__height))

        return Estring

    def __repr__(self):
        """
        Method that returns a string representation of the rectangle,
        that can be used to recreate it
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
