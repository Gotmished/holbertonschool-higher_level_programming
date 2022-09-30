#!/usr/bin/python3
"""
Module containing "save_to_json_file" function
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using
    a JSON representation
    """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
