#!/usr/bin/python3
"""
Module "11-square" including class "Square"
which inherits from "Rectangle" subclass of "BaseGeometry"
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square is a subclass of Rectangle
    which is a subclass of BaseGeometry
    """
    def __init__(self, size):
        """
        Instantiation with size, then rendered private
        and associated with base class
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of a square
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        Informal string representation of a square
        """
        return (f"[Square] {self.__size}/{self.__size}")
