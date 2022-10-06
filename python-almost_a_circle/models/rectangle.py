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
        return self.__width

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public method to return the area of the rectangle instance"""
        return (self.__width * self.__height)

    def display(self):
        """Public method that prints the rectangle using #"""
        for y_position in range(self.__y):
            print()
        for i in range(self.__height):
            for x_position in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}\
/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(args):
            for argv, arg in enumerate(args):
                if argv == 0:
                    self.id = arg
                if argv == 1:
                    self.width = arg
                if argv == 2:
                    self.height = arg
                if argv == 3:
                    self.x = arg
                if argv == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns a dictionary representation of Rectangle"""
        r_dict = {}
        r_dict["id"] = self.id
        r_dict["width"] = self.width
        r_dict["height"] = self.height
        r_dict["x"] = self.x
        r_dict["y"] = self.y
        return r_dict
