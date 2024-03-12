#!/usr/bin/python3
def uppercase(str):
    for i in str:
        uppi = i
        if ord(i) >= 97 and ord(i) <= 122:
            uppi = chr(ord(i) - 32)
        print("{}".format(uppi), end="")
    print("")
