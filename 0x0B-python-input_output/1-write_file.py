#!/usr/bin/python3
"""Module write a file"""


def write_file(filename="", text=""):
    """Read and print a text file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        reader = f.write(text)
        return(reader)
