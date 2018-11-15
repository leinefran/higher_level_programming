#!/usr/bin/python3
"""matrix_divided  module"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix"""

    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if isinstance(num, (int, float)) == False:
                raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
        if isinstance(div,(int, float)) == False:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

        new_matrix = []
        for row in matrix:
            for num in row:
                new_num = "{0:.2f}".format(num/div)
                new_matrix.append(new_num)
        return new_matrix
