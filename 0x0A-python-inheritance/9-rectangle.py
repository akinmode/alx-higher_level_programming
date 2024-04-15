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

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return dimensions of rectangle in string format"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
