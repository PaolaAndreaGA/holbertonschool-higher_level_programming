#!/usr/bin/python3
"""script that adds all args to a Python list"""


from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    newObj= load_from_json_file("add_item.json")
except:
    newObj = []

for args in (argv[1:]):
    newObj.append(args)
    save_to_json_file(newObj, "add_item.json")