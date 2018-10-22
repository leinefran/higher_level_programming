#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Represents a class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Returns the id"""

        if id != None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        my_list = []
        if list_objs is None:
            write_file.write(my_list)
        with open(cls.__name__ + ".json", "w") as write_file:
            for elem in list_objs:
                my_list.append(elem.to_dictionary())
            write_file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json_string
