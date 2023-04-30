#!/usr/bin/python3
"""Module which adds two integer or float numbers"""

def add_integer(a, b=98):
    """Function to add two integer or float number and return their sum"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")

    if isinstance(a, float):
        a //= 1
    if isinstance(b, float):
        b //= 1

    result = a
    result += b
    return result
