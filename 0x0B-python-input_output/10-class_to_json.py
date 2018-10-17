#!/usr/bin/python3
"""a function that returns the dictionary description
   with simple data structure for JSON serialization of an object"""


def class_to_json(obj):
    """Created a class json"""

    my_dictionary = obj.__dict__
    return my_dictionary
