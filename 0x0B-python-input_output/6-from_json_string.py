#!/usr/bin/python3
"""A function that returns an object (Python data structure)
   represented by a JSON string"""


import json


def from_json_string(my_str):
    """Using loads() to deserialize"""

    py_data = json.loads(my_str)
    return py_data
