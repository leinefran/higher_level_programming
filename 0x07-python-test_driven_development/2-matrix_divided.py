#!/usr/bin/python3
"""matrix_divided  module"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix"""

    matrix_len = []
    for row in matrix:
        matrix_len = matrix_len.append(len(row))
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)
            of integers/floats")
        if len(matrix) != len(matrix_len):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if is not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)
                of integers/floats")
        if is not isinstance(div,(int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
