#!/usr/bin/python3
"""a function that writes an Object to a text file,
   using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Using dump() to serialize, with and open()"""
    with open(filename, "w") as write_file:
        json.dump(my_obj, write_file)
