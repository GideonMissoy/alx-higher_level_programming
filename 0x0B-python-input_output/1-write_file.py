#!/usr/bin/python3
"""
Contains the function write_file
Function writes a string to a text file.
"""


def write_file(filename="", text=""):
    """This function writes a string to a text file."""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
