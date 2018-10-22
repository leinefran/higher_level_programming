#!/usr/bin/python3
"""A class Square that inherits from Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square instantiation"""
        super().__init__(size, size, x, y, id=None)
        self.size = size


    @property
    def size(self):
        """Returns the size of the width and height"""
        return super().width

    @size.setter
    def size(self, value):
        """Sets the size attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Overriding the __str__ method"""
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size))
