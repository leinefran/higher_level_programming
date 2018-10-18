#!/usr/byn/python3
"""A function that returns the number of lines of a text file"""


def number_of_lines(filename=""):
    """Getting the line count of a file using readline()"""

    num_lines = 0

    with open(filename, 'r') as f:
        """Using a for loop"""
        for line in f:
            num_lines += 1

    return num_lines
