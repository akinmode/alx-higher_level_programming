#!/usr/bin/python3
"""inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square inherits Rectangle"""

    def __init__(self, size):
        """
            Validates and sets dimensions as private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self._Rectangle__width,
                                           self._Rectangle__height)
