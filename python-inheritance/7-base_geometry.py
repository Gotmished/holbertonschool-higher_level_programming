#!/usr/bin/python3
"""
Module "5-base_geometry" including "BaseGeometry" class
and public instance methods "area" and "integer_validator"
"""


class BaseGeometry:
    """
    A class with public instance method "area"
    """
    def area(self):
        """
        Raises an exception for area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates attribute value associated with attribute name
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
