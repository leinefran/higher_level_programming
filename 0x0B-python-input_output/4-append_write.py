#!/usr/bin/python3
"""A function that appends a string at the end of a text file
   & returns the number of characters added"""


def append_write(filename="", text=""):
    """Using mode a to append"""

    with open(filename, 'a') as f:
        f.write(text)

    return len(text)
