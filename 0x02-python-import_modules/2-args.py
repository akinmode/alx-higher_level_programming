#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    """
        Prints the number of and the list of its arguments.
    """
    argc = len(argv) - 1
    if argc == 0:
        print("{} arguments.".format(argc))
    else:
        if argc == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(argc))
        for i, arg in enumerate(argv[1:], 1):
            print("{}: {}".format(i, arg))
