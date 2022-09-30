#!/usr/bin/python3
"""
Module containing "append_write" function
"""


def append_write(filename="", text=""):
    """
    Appends a string "text" to the end of a file "filename"
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
