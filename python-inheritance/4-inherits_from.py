#!/usr/bin/python3
"""
Module containing the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Returns True or False depending upon whether an object
    is an instance of a subclass of a_class
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
