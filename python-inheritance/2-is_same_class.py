#!/usr/bin/python3
"""
The "is_same_class" function
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is an instance of specified class, exactly.
    False, otherwise.
    """
    return (type(obj) is a_class))
