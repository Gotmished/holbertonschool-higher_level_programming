#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class represents the Square with a certain size"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """Property - returns __size of square"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """Property setter - of __size"""
        self.__size = value

    @property
    def position(self):
        """Property setter - returns __position of square"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """Property setter - of __property"""
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
