#!/usr/bin/python3
"""
This is the "5-text_indentation" module with one function:

text_indentation(text)
"""


def text_indentation(text):
    """
    Prints supplied text with two new lines following
    any instance of '.', '?', and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(". ", ".\n\n")
    text = text.replace("? ", "?\n\n")
    text = text.replace(": ", ":\n\n")
    print(f"{text}", end="")
