#!/usr/bin/python3
"""
Module containing "class_to_json" function
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON
    serialisation of an object in the form of a
    simple data structure (list, dictionary,
    integer, boolean). That is, returns a JSON
    dictionary of a class object
    """
    return obj.__dict__
