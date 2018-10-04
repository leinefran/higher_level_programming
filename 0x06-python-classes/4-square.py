#!/usr/bin/python3
class Square():
        def __init__(self, size=0, area=0):
            try:
                self.__size = size
                self.__area = area
            except TypeError:
                raise TypeError("size must be an interger")
            except ValueError:
                raise ValueError("size must be >= 0")
        def area(self):
            return self.__area
        def size(self):
                pass
