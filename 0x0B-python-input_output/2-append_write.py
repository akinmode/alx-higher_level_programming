#!/usr/bin/python3
""" Appends a string at the end of a text file (UTF8)
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
        Writes a string to a file
    """
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
