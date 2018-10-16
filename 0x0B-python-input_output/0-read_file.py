#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Using the with statement"""

    with open(filename, 'rt') as f:
        read = f.read()
        print(read, end="")
