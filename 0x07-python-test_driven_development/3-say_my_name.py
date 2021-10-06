#!/usr/bin/python3
"""Write a function that prints My name is
"""


def say_my_name(first_name, last_name=""):
    """args: first_name type string,
    last_name type string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
