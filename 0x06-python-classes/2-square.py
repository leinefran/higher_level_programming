#!/usr/bin/python3
class Square():
    try:
        def __init__(self, size=0):
            self.__size = size
    except TypeError:
        print("size must be an interger")
    except ValueError:
        print("size must be >= 0")
