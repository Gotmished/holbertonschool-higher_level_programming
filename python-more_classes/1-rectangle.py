#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """A class for a rectangle of given width and height

    Attributes:
    __width (int): the width of the rectangle
    __height (int): the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Property getter for __width. Returns the width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Property setter for __width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property getter for __height. Returns the height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """Property setter for __height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
