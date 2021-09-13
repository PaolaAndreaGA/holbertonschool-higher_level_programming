#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    copylist = my_list.copy()
    if idx < 0:
        return copylist

    if idx >= len(my_list):
        return copylist

    copylist[idx] = element
    return copylist
