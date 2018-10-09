#!/usr/bin/python3
"""Empty class rectangle"""


class Rectangle:
    """"Represents a class rectangle"""

    def __init__(self, width=0, height=0):
        """Rectangle Instantiation"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width size"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute with error handling"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height size"""
        return self.height

    @height.setter
    def height(self, value):
        """Sets the height attribute with error handling"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        a = self.width * self.height
        return a

    def perimeter(self):
        """Returns the perimeter of a Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        p = 2*(self.width + self.height)
        return p
