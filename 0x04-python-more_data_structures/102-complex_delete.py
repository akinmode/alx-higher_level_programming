#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
        Deletes keys with a specific value in a dictionary.
    """
    if a_dictionary is not None:
        for k, v in a_dictionary.copy().items():
            if v == value:
                del a_dictionary[k]
        return a_dictionary
    else:
        return a_dictionary
