#!/usr/bin/python3
"""
Module containing "Base" class
"""


class Base:
    """
    The base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base class constructor with public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
