#!/usr/bin/python3
"""Module prints a square # of size dimension"""


def print_square(size):
    """Print a square made of #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print('#' * size)
