#!/usr/bin/python3
"""Module write a file
"""


def append_write(filename="", text=""):
    """function that appends a string
    at the end of a text file
    Return: he number of characters added
    """
    with open(filename, mode='a', encoding="utf-8") as  f:
        str_count = f.write(text)
    return str_count
