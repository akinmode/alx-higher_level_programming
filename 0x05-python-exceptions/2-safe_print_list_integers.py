#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
        Prints the first x elements of a list and only integers
    """
    realn = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            realn += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print()
    return realn
