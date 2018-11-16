#!/usr/bin/python3
"""matrix_divided  module"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix"""

    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list" +
                        "f lists) of integers/floats")

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list" +
                            "of lists) of integers/floats")
    length_list = []
    for row in matrix:
        length_list.append(len(row))

    for i in range(len(length_list) - 1):
        if length_list[i] != length_list[i + 1]:
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for num in row:
            if isinstance(num, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list" +
                                "of lists) of integers/floats")
        if isinstance(div, (int, float)) is False:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

        new_matrix = []
        for row in matrix:
            tmp = []
            for num in row:
                num = num/div
                tmp.append(round(num, 2))
            new_matrix.append(tmp)
        return new_matrix
