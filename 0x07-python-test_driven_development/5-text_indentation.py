#!/usr/bin/python3
"""
Write a function that prints a text with 2 new
lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    x = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if x == 1 and i is ' ':
            print('', end='')
            x = 0
            continue
        if i is '.' or i is '?' or i is ':':
            print("{}\n". format(i))
            x = 1
        else:
            print(i, end='')
            x = 0
