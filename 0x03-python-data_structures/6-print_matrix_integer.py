#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for i in row:
            if count == len(row)-1:
                print("{:d}".format(i), end='')
            else:
                print("{:d}".format(i), end=' ')
            count += 1
        print()
