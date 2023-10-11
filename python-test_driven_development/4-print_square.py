#!/usr/bin/python3

'''

    Module to test doctest module with a simple function which
    print the area of the square
'''


def print_square(size):

    '''

    Function that prints the
    area of the square
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
