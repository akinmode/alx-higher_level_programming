#!/usr/bin/python3
for i in range(0, 98):
    if i % 10 > i // 10:
        print(f"{i:02}", end=", ")
print(f"{89}")
