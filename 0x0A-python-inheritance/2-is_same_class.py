#!/usr/bin/python3
"""is_same_class module"""
def is_same_class(obj, a_class):
    """checks if a object is an instance of specified class"""
    if type(obj) is object:
        return False
    return isinstance(obj, a_class)
