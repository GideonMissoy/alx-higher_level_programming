#!/usr/bin/python3
"""
Module defines function text_indentation(text)
Function prints a text with 2 new lines after: ('.', '?', ':')
"""


def text_indentation(text):
    special = ['.', '?', ':']
    if type(text) != str:
        raise TypeError("text must be a string")
    for i, s in enumerate(text):
        print(s, end='')
        if s in special:
            # Check if there are white spaces after the special character
            if i + 1 < len(text) and text[i + 1].isspace():
                # Find the index of the first non-white space character
                j = i + 1
                while j < len(text) and text[j].isspace():
                    j += 1
                # Print two new lines after skipping the white spaces
                print('\n\n', end='')
                # Update the loop index to skip the white spaces
                i = j - 1
            else:
                print('\n\n', end='')
