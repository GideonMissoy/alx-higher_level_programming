#!/usr/bin/python3
"""
Module contains a class Student.
"""


class Student:
    """Representation of a student."""
    def __init__(self, first_name, last_name, age):
        """Initializes the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict rep of a Student instance."""
        return self.__dict__
