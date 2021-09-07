#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        letter = ord(str)
        if letter >= 97 and letter <= 122:
            letter -= 32
        letter = chr(letter)
        print("{:c}".format(letter), end='')
    print(" ")
