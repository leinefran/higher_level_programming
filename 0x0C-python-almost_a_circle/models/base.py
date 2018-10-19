#!/usr/bin/python3
"""Base class"""


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
