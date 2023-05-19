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

    def to_json(self):
        """
        Public instance method returning a JSON
        dictionary of a student instance
        """
        return self.__dict__
