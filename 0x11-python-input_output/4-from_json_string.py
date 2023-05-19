#!/usr/bin/python3
"""
Module containing "from_json_string" function
"""


def from_json_string(my_str):
    """
    Returns a data structure from a JSON string
    """
    import json
    return json.loads(my_str)
