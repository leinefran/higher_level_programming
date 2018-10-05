#!/usr/bin/python3
class Square():
        """Created a square"""
        def __init__(self, size=0, area=0):
                """Square instantiation"""
                self.__size = size
                self.__area = area

        def size(self):
                return self.__size

        def size(self, size=0):
                if type(size) is not int:
                        raise TypeError("size must be an interger")
                if size < 0:
                        raise ValueError("size must be >= 0")

        def area(self):
            return self.__size * self.__size
