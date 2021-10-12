#!/usr/bin/python3
"""Module write a file
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    (UTF8) and returns the number of characters written
    """
    with open(filename, encoding="utf-8") as f:
        readata = f.write(text)
        return(readata)
