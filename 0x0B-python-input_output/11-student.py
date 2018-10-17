#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """Represents a class student"""

    def __init__(self, first_name, last_name, age):
        """Student Instantiation"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""

        my_dict = self.__dict__
        return my_dict
