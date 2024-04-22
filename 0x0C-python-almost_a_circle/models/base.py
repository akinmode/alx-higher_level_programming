#!/usr/bin/python3
""" Base Geometry Module
    to manage attribute in all classes
    and avoid code duplication
"""


class Base:
    """Base Geometry Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
