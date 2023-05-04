#!/usr/bin/python3
"""
MyList class that inherits from list
"""


class MyList(list):
    """subclass of list initializes"""
    def __init__(self):
        """Initializes the object we have"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list in order"""
        print(sorted(self))
