#!/usr/bin/python3
"""
Module "8-rectangle" including class "Rectangle"
which inherits from "BaseGeometry" class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is a subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height, then rendered private
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
