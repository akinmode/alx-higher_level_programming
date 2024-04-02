#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
        Divides element by element 2 lists
    """
    divlist = []
    for x in range(list_length):
        try:
            divlist.append(my_list_1[x] / my_list_2[x])
        except TypeError:
            print("wrong type")
            divlist.append(0)
            continue
        except ArithmeticError:
            print("division by 0")
            divlist.append(0)
            continue
        except IndexError:
            print("out of range")
            divlist.append(0)
            continue
        finally:
            pass
    return divlist
