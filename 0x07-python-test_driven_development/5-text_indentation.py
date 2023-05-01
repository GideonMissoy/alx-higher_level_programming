#!/usr/bin/python3#!/usr/bin/python3

def text_indentation(text):
    """Indents the sentences in a string by adding extra lines and removing leading whitespace."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Replace all sentence-ending punctuation with the punctuation followed by two newlines
    sentences = ''
    for char in text:
        if char in '.?!':
            sentences += char + '\n\n'
        elif char == ':':
            sentences += char + '\n'

        else:
            sentences += char

    # Split the resulting string into a list of lines, remove leading whitespace, and re-join the lines
    indented_lines = [line.lstrip() for line in sentences.splitlines()]
    indented_text = '\n'.join(indented_lines)

    # Return the resulting string
    return indented_text
