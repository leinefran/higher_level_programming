#!/usr/bin/python3
"""print_square module"""


def print_square(size):
    """a function that prints a square with the character #"""

    #size is the size length of the square

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    #print:
    rec = ""
    for i in range(size):
        print("#" * size)
