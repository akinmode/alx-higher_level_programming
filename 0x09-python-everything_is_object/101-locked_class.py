#!/usr/bin/python3
"""Module contains class LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name"""


class LockedClass:
    """Class with locked down attributes"""

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
        else:
            self.__dict__[name] = value
