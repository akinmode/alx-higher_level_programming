#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
        Prints a matrix of integers.
    """
    for row in matrix:
        if row is not None and row != []:
            for col in row[:-1]:
                print("{:d}".format(col), end=' ')
            print("{:d}".format(row[-1]))
        else:
            print()
