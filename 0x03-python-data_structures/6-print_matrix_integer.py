#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for i in range(matrix):
        for j in range(i):
            print("{:d}".format(i), end='')
            if j != (i[len(i)-1]):
                print('', end=' ')
        print('')
