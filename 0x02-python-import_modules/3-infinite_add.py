#!/usr/bin/python3
import sys


if __name__ == "__main__":
    argc = len(sys.argv)
    total = 0
    for num in range(1, argc):
        total = total + int(sys.argv[num])
    print(total)
