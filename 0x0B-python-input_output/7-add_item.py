#!/usr/bin/python3
""" Adds all arguments to a Python list, and then save them to a file """
import os
import sys
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file

if os.path.exists('add_item.json'):
    mylist = load_from_json('add_item.json')
else:
    mylist = []

for i in range(1, len(sys.argv)):
    mylist.append(sys.argv[i])

save_to_json(mylist, 'add_item.json')
