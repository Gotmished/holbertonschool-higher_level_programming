#!/usr/bin/python3
"""
Module containing "write_file" function
"""


def write_file(filename="", text=""):
    """
    writes a string "text" to a file "filename" and
    returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
