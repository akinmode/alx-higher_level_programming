#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
        Replaces all occurrences of an element by another in a new list.
    """
    if my_list is not None:
        return [replace if i == search else i for i in my_list]
