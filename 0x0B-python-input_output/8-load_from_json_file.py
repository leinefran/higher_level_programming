#!/usr/bin/python3
"""A function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Using loads to deserialize, with & open()"""

    my_obj = ""
    with open(filename, 'r') as ob:
        while True:
            line = ob.readline()
            if not line:
                break
            my_obj += line

    py_data = json.loads(my_obj)
    return py_data
