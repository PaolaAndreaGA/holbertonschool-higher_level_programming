#!/usr/bin/python3
"""Module add item
"""
import json
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    new = load_from_json_file(filename)
except (ValueError, FileNotFoundError):
    new = []
for args in sys.argv[1:]:
    new.append(args)
save_to_json_file(new, filename)
