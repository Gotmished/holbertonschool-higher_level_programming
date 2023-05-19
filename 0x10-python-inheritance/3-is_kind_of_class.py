#!/usr/bin/python3
"""
Module contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True or False depending upon whether object is
    an instance of a class, or an instance of a class inherited
    from a specific class
    """
    return (isinstance(obj, a_class))
