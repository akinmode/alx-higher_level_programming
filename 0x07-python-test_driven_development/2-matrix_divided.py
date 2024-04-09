#!/usr/bin/python3
"""Module returns the result of a matrix divided by a scalar"""


def matrix_divided(matrix, div):
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    nrow = len(matrix[0])
    newmatrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(row) != nrow:
            raise TypeError("Each row of the matrix must have the same size")
        newrow = []
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            newrow.append(round(float(x / div), 2))
        newmatrix.append(newrow)
    return newmatrix
