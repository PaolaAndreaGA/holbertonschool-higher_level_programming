#!/usr/bin/python3
""" Module pascal triangle
"""


def pascal_triangle(n):
    """function  that returns a
    list of lists of integers representing
    the Pascal’s triangle of n:
    """
    triangle_list =[]
    if n <= 0:
        return triangle_list
    for i in range(n):
        item = 11**i
        l = [int(n) for n in str(item)]
        triangle_list.append(l)
    return triangle_list
