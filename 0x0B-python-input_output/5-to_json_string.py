#!/usr/bin/python3
"""A function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Using dumps() to serialize"""
    json_string = json.dumps(my_obj)
    return json_string
