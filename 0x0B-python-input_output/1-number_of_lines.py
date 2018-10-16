#!/usr/byn/python3
"""A function that returns the number of lines of a text file"""


def number_of_lines(filename=""):
    """Getting the line count of a file using enumerate()"""

    lines = 0

    with open(filename, 'rt') as f:
        while True:
            read = f.readline()
            lines += 1
            if not read:
                break
    return lines
