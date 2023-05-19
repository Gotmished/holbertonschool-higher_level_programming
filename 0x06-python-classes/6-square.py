#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class represents a square with a certain size and position in space

    Attributes:
    __size (int): the size of the square
    __position (tuple): the position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialises the square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Property - returns __size of square"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """Property setter - of __size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Property setter - returns __position of square in (x, y)"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """Property setter - of __property"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Public instance method - returns the area of the Square"""
        return(self.__size * self.__size)

    def my_print(self):
        """Public instance method - prints square with #"""
        if self.__size == 0:
            print()
            return

        for y_position in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for x_position in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
