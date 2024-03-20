#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
        Deletes a key in a dictionary.
    """
    if a_dictionary is not None and key in a_dictionary.keys():
        a_dictionary.pop(key)
        return a_dictionary
    else:
        return a_dictionary
