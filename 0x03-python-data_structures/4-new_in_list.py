#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
        Replaces an element in a list at a specific position
        without modifying the original list (like in C).
    """
    if my_list is not None or idx is not None:
        my_listc = my_list.copy()

        if idx < 0 or idx >= len(my_listc):
            return my_listc
        else:
            my_listc[idx] = element
            return my_listc
    else:
        return
