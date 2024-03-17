#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
        Finds all multiples of 2 in a list.
    """
    if my_list is not None:
        return [i % 2 == 0 for i in my_list]
    else:
        return None
