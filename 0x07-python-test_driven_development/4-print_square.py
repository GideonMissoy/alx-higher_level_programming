#!/usr/bin/python3
"""
Module which prints a square using '#' character
"""


def print_square(size):
    """Prints a square made of '#' characters of given size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        print("{}".format('#' * size))
