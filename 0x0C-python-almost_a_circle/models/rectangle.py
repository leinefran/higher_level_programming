#!/usr/bin/python3
"""A class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represents a class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle Instantiation"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """Returns the width size"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height size"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        a = self.__width * self.__height
        return a

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        rect = []
        for i in range(self.height):
            rect.append("#" * self.width)
        print("\n".join(rect))
