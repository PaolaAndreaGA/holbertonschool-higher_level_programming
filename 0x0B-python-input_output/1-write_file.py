#!/usr/bin/python3
"""Module write a file
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    (UTF8) and returns the number of characters written
    """
    with open(filename, encoding='UTF8') as f:
        for line in f:
            count = count + 1
    return count
