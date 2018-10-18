#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """Represents a class student"""

    def __init__(self, first_name, last_name, age):
        """Student Instantiation"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""

        """If attrs is a list of strings, only attributes name contain in this
        list must be retrieved."""
        if not isinstance(attrs, list):
            return self.__dict__

        for element in attrs:
            if not isinstance(element, str):
                return self.__dict__

        result = {}
        for k, v in self.__dict__.items():
            if k in attrs:
                result[k] = v
        return result

    def reload_from_json(self, json):
        """A public method that replaces all attributes of an instance"""
        """Overrrinding a method"""

        for key in json:
            self.__dict__.update({key: json.get(key)})
