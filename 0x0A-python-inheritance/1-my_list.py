#!/usr/bin/python3
"""
MyList inherits list.
"""


class MyClass(list):
    """
    Subclass of list that provides additional functionalities.

    This class extends the functionality of the built-in list class.
    It adds a method to print the list in sorted order.
    """

    def __init__(self):
        """
        Initializes an instance of MyClass.
        """
        super().__init__()

    def print_sorted(self):
        """
        This method sorts the list in ascending order using the sorted function
        and then prints the sorted list.
        """
        print(sorted(self))

