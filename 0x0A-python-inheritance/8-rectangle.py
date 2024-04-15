#!/usr/bin/python3
"""inherits from BaseGeomentry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits BaseGeometry"""

    def __init__(self, width, height):
        """
            Validates and sets dimensions as private
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
