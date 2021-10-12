#!/usr/bin/python3
"""Module add item
"""
import json
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
present = os.path.isfile(filename)

if present:
    mylist = load_from_json_file(filename)
else:
    mylist = []

for args in sys.argv:
    if args == "./9-add_item.py":
        continue
    mylist.append(args)
save_to_json_file(mylist, filename)
