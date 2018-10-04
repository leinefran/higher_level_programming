#!/usr/bin/python3
class Square():
        def __init__(self, size=0):
            try:
                self.__size = size
            except TypeError:
                raise TypeError("size must be an interger")
            except ValueError:
                raise ValueError("size must be >= 0")
