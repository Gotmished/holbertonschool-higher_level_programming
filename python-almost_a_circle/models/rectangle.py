#!/usr/bin/python3
"""
Module containing class "Rectangle" that inherits
from base class "Base"
"""
from models.base import Base


class Rectangle(Base):
    """A class that represents a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for instantiation of a rectangle.
        Super class called with id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__height

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.__y = value
