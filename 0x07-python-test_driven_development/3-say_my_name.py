#!/usr/bin/python3
"""
Module defines function say_my_name(first_name, last_name="")
Function prints 'My name is <first_name> <last_name>'
"""


def say_my_name(first_name, last_name=""):
    """prints a formatted name, with optional last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last name must be a string")
    print("My name is", first_name, last_name)
