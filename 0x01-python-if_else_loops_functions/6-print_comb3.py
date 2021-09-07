#!/usr/bin/python3
for nl in range(0, 10):
    for nr in range(nl + 1, 10):
        if nl == 8 and nr == 9:
            print("{:d}{:d}".format(nl, nr))
        else:
            print("{:d}{:d}, ".format(nl, nr), end='')
