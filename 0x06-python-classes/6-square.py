#!/usr/bin/python3
""""Module Square"""


class Square():
    """Created a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Square instantiation"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """"Size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    @property
    def position(self):
        """Position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for j in range(self.size):
                if self.position[0] > 0:
                    print(" " * self.position[0], end="")
                print("#" * self.size)
