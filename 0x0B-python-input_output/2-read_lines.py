#!/usr/bin/python3
"""A function that reads n lines of a text file (UTF8) & prints it to stdout"""


def read_lines(filename="", nb_lines=0):
    """Using realine()"""

    text = ""

    with open(filename, 'rt') as f:
        if nb_lines <= 0 or nb_lines >= len(open(filename).readlines()):
            read = f.read()
            print(read,end="")
        while nb_lines:
            read = f.readline()
            nb_lines -= 1
            text += read
        print(text, end="")
