#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """A class for a rectangle of given width and height

    Public Class Attributes:
    number_of_instances (int): a count of instantiation minus deletion
    print_symbol (any type): a symbol used when printing the rectangle

    Private Instance Attributes:
    __width (int): the width of the rectangle
    __height (int): the height of the rectangle
    """

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the greatest area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return(rect_1)
        else:
            return(rect_2)

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialises the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Property getter for __width. Returns the width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Property setter for __width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property getter for __height. Returns the height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """Property setter for __height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method returning the area"""
        return(self.width * self.height)

    def perimeter(self):
        """Public instance method returning the perimeter"""
        if self.width == 0 or self.height == 0:
            return(0)
        return(2 * (self.width + self.height))

    def __str__(self):
        """Returns a printable string representation of a rectangle"""
        r_str = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                for j in range(self.width):
                    r_str = r_str + str(self.print_symbol)
                if i != self.height - 1:
                    r_str = r_str + "\n"
        return(r_str)

    def __repr__(self):
        """Returns a reproducible string representation of a rectangle"""
        return(f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
