#!/usr/bin/python3
""" Class inherits integer """


class MyInt(int):
    """ Reverses an integer """
    def __init__(self, myint):
        self.__myint = myint

    def __eq__(x1, x2):
        return x1.__myint != x2

    def __ne__(x1, x2):
        return x1.__myint == x2
