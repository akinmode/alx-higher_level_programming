#!/usr/bin/python3
for i in range(90, 64, -1):
    print("{:c}".format(i + ((i + 1) % 2) * 32), end="")
