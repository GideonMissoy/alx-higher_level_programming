#!/usr/bin/python3
"""
Module defines function text_indentation(text)
Function prints a text with 2 new lines after: ('.', '?', ':')
"""


def text_indentation(text):
    """prints a text with 2 new lines after . ? :"""
    special = ['.', '?', ':']
    if type(text) != str:
        raise TypeError("text must be a string")
    for s in text:
        print(s, end='')
        if s in special:
            print('\n\n', end='')
