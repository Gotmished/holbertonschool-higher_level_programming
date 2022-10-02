#!/usr/bin/python3
"""
Module containing "Student" class
"""


class Student:
    """
    Representation of a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation of a student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public instance method returning a JSON
        dictionary of a student instance. If attrs is
        a list of strings, a new dictionary is returned
        comprising only the attributes from attrs
        """
        if attrs is None:
            return self.__dict__
        else:
            if isinstance(attrs, list):
                for element in attrs:
                    if not isinstance(element, str):
                        return self.__dict__
                    else:
                        return {element: self.__dict__[element]
                                for element in attrs if
                                hasattr(self, element)}
