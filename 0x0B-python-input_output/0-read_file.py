#!/usr/bin/python3
"""Read a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
        Return the contents of a file
    """
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read(), end="")
