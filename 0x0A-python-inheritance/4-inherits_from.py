#!/usr/bin/python3
""" Checks for direct inheritance"""


def inherits_from(obj, a_class):
    """
        Returns True if the object is an instance
        of a class that inherited (directly or indirectly)
        from the specified class otherwise False.
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
