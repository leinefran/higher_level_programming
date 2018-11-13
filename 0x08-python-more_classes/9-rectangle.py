#!/usr/bin/python3
"""Empty class rectangle"""


class Rectangle:
    """"Represents a class rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Rectangle Instantiation"""
        type(self).number_of_instances += 1

        self.width = width
        self.height = height

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
        return self.__height

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
                rect += str(self.print_symbol)
            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """"Returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return False

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance"""
        return cls(width=size, height=size)
