#!/usr/bin/python3
"""
Module containing "to_json_string" function
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of a string
    """
    import json
    return json.dumps(my_obj)
