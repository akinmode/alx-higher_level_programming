#!/usr/bin/python3
def no_c(my_string):
    """
        Removes all characters c and C from a string.
    """
    my_stringn = ""
    for i in my_string:
        if (i != 'c') & (i != 'C'):
            my_stringn += i
    return my_stringn
