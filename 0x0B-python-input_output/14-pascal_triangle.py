#!/usr/bin/python3
"""A function that returns a list of lists of integers
   representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """A method"""

    if n <= 0:
        return [[]]

    my_list = [[]]

    for i in range(n):
        nested_list = []
        for j in range(i + 1):
            if j == 0:
                nested_list += [1]
            elif j == i:
                nested_list += [1]
            else:
                nested_list = my_list[i - 1][j - 1] + my_list[i - 1][j]

        my_list += nested_list

    return my_list
