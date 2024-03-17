#!/usr/bin/python3
def element_at(my_list, idx):
    """
        Retrieves an element from a list like in C.
    """
    if my_list is not None or idx is not None:
        if idx < 0 or idx >= len(my_list):
            return None
        else:
            return my_list[idx]
    else:
        return
