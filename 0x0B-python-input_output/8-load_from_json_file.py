#!/usr/bin/python3
"""A function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Using load()"""

    with open(filename, 'r') as f:
        return json.load(f)
