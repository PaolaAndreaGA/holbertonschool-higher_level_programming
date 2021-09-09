#!/usr/bin/python3qss
import hidden_4

if __name__ == "__main__":
    file = dir(hidden_4)
    length = len(file)
    for name in range(0, length):
        if file[name][0:2] != "__":
            print(file[name])
