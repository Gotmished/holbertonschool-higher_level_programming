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

    flag = 0
    for char in range(len(text)):
        if flag == 1:
            char = char + 1
            if text[char] != ' ':
                flag = 0
        else:
            print(f"{text[char]}", end="")
            if text[char] in [".", ":", "?"]:
                print("\n")
                if text[char + 1] == ' ':
                    flag = 1
                    continue
                else:
                    flag == 0
