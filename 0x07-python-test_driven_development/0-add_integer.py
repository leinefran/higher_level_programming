#!/usr/bin/python3
"""add_integer module"""


def add_integer(a, b=98):
    """Adds 2 integers. If the 2nd argv is not provided,
    it is set to 98 by default
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an interger")
    if type(a) == float or type(b) == float:
        return int(a) + int(b)

    return a + b
