#!/usr/bin/python3
"""
Module defines function text_indentation(text)
Function prints a text with 2 new lines after: ('.', '?', ':')
"""


def text_indentation(text):
    """prints a text with 2 new lines after . ? :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for t in text:
        if flag == 0:
            continue
        else:
            flag = 1
        if flag == 1:
            if t == '?' or t == '.' or t == ':':
                print(t)
                print()
                flag = 0
            else:
                print(t, end="")
