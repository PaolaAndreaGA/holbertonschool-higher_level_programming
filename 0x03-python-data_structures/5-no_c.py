#!/usr/bin/env python3


def no_c(my_string):
    Nstr = ""
    for i in my_string:
        if i is not "c" and i is not "C":
            Nstr = Nstr + i
    return Nstr
