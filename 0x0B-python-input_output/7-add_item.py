#!/usr/bin/python3
"""Module add item
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    new = load_from_json_file(filename)
except Exception:
    new = []
new.extend(sys.args[1:])
save_to_json_file(new, filename)
