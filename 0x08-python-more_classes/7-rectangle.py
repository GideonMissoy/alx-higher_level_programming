#!/usr/bin/python3
"""
class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """Rectangle information: width, height"""
    number_of_instances = 0
    print_symbol = "#"  # class variable

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Destructor that prints a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter method for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns a string representation of the rectangle"""
        Estring = ""
        if self.__width != 0 and self.__height != 0:
            Estring += "\n".join(str(self.print_symbol) * self.__width
                                for i in range(self.__height))
        return Estring

    def __repr__(self):
        """
        Returns a string representation of the rectangle for debugging purposes
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
