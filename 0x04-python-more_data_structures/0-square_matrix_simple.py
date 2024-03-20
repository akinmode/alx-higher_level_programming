#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
        Computes the square value of all integers of a matrix.
    """
    if matrix is not None:
        return list(list(map(lambda col: col ** 2, row)) for row in matrix)
