#!/usr/bin/python3

def print_text(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Initialize a flag to indicate whether the previous character
    #was a sentence-ending punctuation
    prev_punct = False
    
    # Iterate over each character in the input string
    for char in text:
        # If the character is a sentence-ending punctuation,
        # print it with two newlines and set the flag to True
        if char in ".?!":
            print(char, end="")
            print("\n\n", end="")
            prev_punct = True
        # If the character is a colon, print it with a newline and set the flag to True
        elif char == ":":
            print(char, end="")
            print("\n\n", end="")
            prev_punct = True
        # If the character is not a sentence-ending punctuation or a colon, print it normally
        else:
            # If the previous character was a sentence-ending punctuation,
            # print the current character on a new line
            if prev_punct:
                print(char, end="")
                print("\n", end="")
                prev_punct = False
            # If the previous character was not a sentence-ending punctuation,
            # print the current character normally
            else:
                print(char, end="")
                prev_punct = False
    # If the last character was a sentence-ending punctuation or a colon, print an extra newline
    if prev_punct:
        print("\n", end="")
