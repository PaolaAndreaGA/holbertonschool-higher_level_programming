#!/usr/bin/python3
"""Module string representation from json
"""
import json


def from_json_string(my_str):
    """Write a function that returns an object
       represented by a JSON string
    """
    return (json.load(my_str))
