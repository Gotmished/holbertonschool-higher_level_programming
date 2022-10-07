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
    def from_json_string(json_string):
        """Returns a list from the JSON representation"""
        if json_string is None or not len(json_string):
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None or not len(list_dictionaries):
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON representation of a list of instances to a file.
        That is, serialises the list
        """
        list_ob = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for entry in list_objs:
                list_ob.append(entry.to_dictionary())

        with open(filename, "w", encoding="UTF-8") as f:
            f.write(cls.to_json_string(list_ob))

    @classmethod
    def load_from_file(cls):
        """Returns a deserialised list of instances"""
        list_ob = []
        filename = cls.__name__ + ".json"
        if filename:
            with open(filename, "r") as f:
                list_ob = cls.from_json_string(f.read())
                for element, value in enumerate(list_ob):
                    list_ob[element] = cls.create(**list_ob[element])
        return list_ob

    @classmethod
    def create(cls, **dictionary):
        """
        Using a dummy instance, returns an
        instance with pre-set attributes using kwargs
        """
        if cls.__name__ == "Square":
            dummy = cls(8)
        elif cls.__name__ == "Rectangle":
            dummy = cls(8, 8)
        dummy.update(**dictionary)
        return dummy
