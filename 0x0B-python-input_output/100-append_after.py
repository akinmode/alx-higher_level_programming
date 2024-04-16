#!/usr/bin/python3
""" Inserts a line of text to a file,
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
        Inserts a line of text to a file,
        after each line containing a specific string
    """
    with open(filename, 'r+', encoding='utf8') as f:
        text = ""
        for line in f:
            if search_string in line:
                line += new_string
            text += line
        f.seek(0)
        f.write(text)
