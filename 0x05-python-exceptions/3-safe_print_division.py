#!/usr/bin/python3
def safe_print_division(a, b):
    """
        Divides 2 integers and prints the result (dividend)
    """
    try:
        dividend = a / b
    except ArithmeticError:
        dividend = None
    finally:
        print("Inside result: {}".format(dividend))
    return dividend
