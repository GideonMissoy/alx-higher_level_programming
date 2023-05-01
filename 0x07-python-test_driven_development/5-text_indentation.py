#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with two new lines after each occurrence of ".", "?", or ":"."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ''
    for char in text:
        if char in '.?:':
            new_text += char + '\n\n'
        else:
            new_text += char

    print(new_text)
