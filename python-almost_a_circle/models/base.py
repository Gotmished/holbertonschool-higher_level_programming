#!/usr/bin/python3
"""
Module containing "Base" class
"""

import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries"""
        if not len(list_dictionaries):
            list_dictionaries = []
        return json.dumps(list_dictionaries)
