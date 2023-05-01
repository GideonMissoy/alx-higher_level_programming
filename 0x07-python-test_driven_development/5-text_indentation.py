#!/usr/bin/python3

def text_indentation(text):
    """
    Prints the input text with two newlines after each of these characters:
    '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Replace sentence-ending punctuation with the punctuation,
    # followed by two newlines
    sentences = ''
    for char in text:
        if char in '.?:':
            sentences += char + '\n\n'
        else:
            sentences += char

    # Split the resulting string into a list of lines,
    # remove leading and trailing whitespace, and print each line
    lines = [line.strip() for line in sentences.splitlines()]
    for line in lines:
        print(line)
