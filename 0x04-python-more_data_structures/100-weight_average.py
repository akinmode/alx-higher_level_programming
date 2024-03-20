#!/usr/bin/python3
def weight_average(my_list=[]):
    """
        returns the weighted average of all
        integers tuple (<score>, <weight>)
    """
    if my_list is not None and my_list != []:
        weight = 0
        sum_total = 0
        for x, y in my_list:
            weight += y
            sum_total += y * x
        return sum_total/weight
    else:
        return 0
