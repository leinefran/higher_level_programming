#!/usr/bin/python3
"""Module Square"""


class Square():
        """created a square"""

    def __init__(self, size=0):
        """Inits Class"""
        if type(size) is not int:
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
