#!/usr/bin/python3
"""
This module contains function append_write
Function appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """function appends a string at the end of a text file."""
    with open(filename, 'a', encoding="utf8") as file:
        return file.write(text)
