#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = []
    for num in my_list:
        if (num % 2) == 0:
            new_list.append(True)
        elif  my_list[num] % 1 == 0:
            new_list.append(False)
    return new_list
