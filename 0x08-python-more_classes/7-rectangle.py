#!/usr/bin/python3
"""Contains the rectangle class"""


class Rectangle:
    """A Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            Initialize the dimensions of a rectangle
        """
        self.width = width
        self.height = height
        self.number_of_instances += 1

    @property
    def width(self):
        """Width property function"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Height property function"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def __str__(self):
        """Returns # representation
        of the dimensions of a rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        string = ""
        for y in range(self.height - 1):
            string += str(self.print_symbol) * self.width + '\n'
        string += str(self.print_symbol) * self.width
        return string

    def __repr__(self):
        """Returns repr of the rectangle"""
        string = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return string

    def __del__(self):
        """Delete a rectangle"""
        print("Bye rectangle...")
        if self.number_of_instances != 0:
            self.number_of_instances -= 1

    def area(self):
        """Returns area of a rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2
