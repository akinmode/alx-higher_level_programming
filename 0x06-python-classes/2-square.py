#!/usr/bin/python3
"""Defines the square class"""


class Square:
    """Square class. Has a private size"""
    def __init__(self, size=0):
        """Initialize Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
