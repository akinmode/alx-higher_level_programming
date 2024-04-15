#!/usr/bin/python3
""" A BaseGeometry Class """


class BaseGeometry:
    """ A BaseGeometry class """
    def area(self):
        """
            Returns area of geometry object if implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validates if the value is an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
