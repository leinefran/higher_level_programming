#!/usr/byn/python3
"""A function that returns the number of lines of a text file"""


def number_of_lines(filename=""):
    """Getting the line count of a file using readlines()"""

    lines = 0

    with open(filename, 'rt') as f:
        """Readlines() read a line at a time,
        & returns a list of 1-line strings"""
        read = f.readlines()

    return len(read)
