#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class represents a square with a certain size

    Attributes:
    __size (int): the size of the square
    """

    def __init__(self, size=0):
        """Initialises the square"""
        self.__size = size

    @property
    def size(self):
        """Property - returns __size of square"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """Property setter - of __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method - returns the area of the square"""
        return(self.__size * self.__size)

    def my_print(self):
        """Public instance method - prints square with #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
