#!/usr/bin/python3
for i in range(0, 98):
    if i % 10 > i // 10:
        print("{:02}".format(i), end=", ")
print(f"{89}")
