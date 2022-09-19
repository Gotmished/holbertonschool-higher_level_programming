#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class represents the Square with a certain size"""
    def __init__(self, size=0):
        """Initialises the Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
