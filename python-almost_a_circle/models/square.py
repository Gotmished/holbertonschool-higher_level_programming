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
        return self.height

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.height = value
        self.width = value
