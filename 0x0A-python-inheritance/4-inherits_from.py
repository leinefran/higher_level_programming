#!/usr/bin/python3
"""inheritance module"""


def inherits_from(obj, a_class):
    """checks if an obj is an instance of a class"""

    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
