#!/usr/bin/python3
"""A function that writes a string to a text file
   & returns the number of characters written"""


def write_file(filename="", text=""):
    """Using with and write()"""

    with open(filename, 'wt') as f:
        write = f.write(text)
    return len(text)
