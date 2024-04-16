#!/usr/bin/python3
""" Returns a list of lists of integers representing
    the Pascal’s triangle of n """


def pascal_triangle(n):
    """
        Returns a list of lists of integers
    """
    if n <= 0:
        return []
    n -= 1
    triangle = []
    for row in range(n + 1):
        triangle.append([])
        triangle[row].append(1)
        for col in range(int(row / 2)):
            triangle[row].append(triangle[row - 1][col] +
                                 triangle[row - 1][col + 1])
        if row % 2 == 1:
            triangle[row].extend(triangle[row][::-1])
        else:
            triangle[row].extend(triangle[row][-2::-1])
    return triangle
