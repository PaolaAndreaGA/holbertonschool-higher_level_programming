#!/usr/bin/python3


def no_c(my_string):
    Nstr = ""
    size = len(my_string)
    for i in range(size):
        if my_string[i] != "c" and my_string[i] != "C":
                Nstr += my_string[i]
    return Nstr
