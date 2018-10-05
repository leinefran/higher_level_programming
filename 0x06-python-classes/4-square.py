#!/usr/bin/python3
class Square():
        """Created a square"""
        def __init__(self, size=0, area=0):
                """Square instantiation"""
                if type(size) is not int:
                        raise TypeError("size must be an interger")
                if size < 0:
                        raise ValueError("size must be >= 0")

                self.__size = size

        def size(self):
                return self.__size

        def size(self, value):
                if type(value) is not int:
                        raise TypeError("size must be an interger")
                if value < 0:
                        raise ValueError("size must be >= 0")

                self.__size = value


        def area(self):
            return self.__size ** 2
