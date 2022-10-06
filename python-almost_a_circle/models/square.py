#!/usr/bin/python3
"""
Module containing "Square" subclass that inherits
from "Rectangle" subclass of "Base" class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for instantiation of a rectangle
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        String representation of a square
        """
        return(f"[Square] ({self.id}) {self.x}/\
{self.y} - {self.height}")

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(args):
            for argv, arg in enumerate(args):
                if argv == 0:
                    self.id = arg
                if argv == 1:
                    self.size = arg
                if argv == 2:
                    self.x = arg
                if argv == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        s_dict = {}
        s_dict["id"] = self.id
        s_dict["size"] = self.size
        s_dict["x"] = self.x
        s_dict["y"] = self.y
        return s_dict
