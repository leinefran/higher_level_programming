#!/usr/bin/python3
"""Empty class rectangle"""


class Rectangle:
    """"Represents a class rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Rectangle Instantiation"""
        type(self).number_of_instances += 1


        self.__width = width
        self.__height = height

    @property
    def width(self):
        """"Returns the width size"""
        return self.__width

    @width.setter
    def width(self, value):
        """"Sets the width attribute with error handling"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """"Returns the height size"""
        return self.height

    @height.setter
    def height(self, value):
        """"Sets the height attribute with error handling"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """"Returns the area of the rectangle"""
        a = self.__width * self.__height
        return a

    def perimeter(self):
        """"Returns the perimeter of a Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        p = 2*(self.__width + self.__height)
        return p

    def __str__(self):
        """"Prints in stdout the rectangle with the char #"""
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            rect += "\n"
        return rect

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
