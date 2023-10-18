#!/usr/bin/python3

'''
Python module for demostrative purpose
'''


def read_file(filename=""):
    '''
    Simple function for reading specified file
    '''

    with open(filename, 'r', encoding="utf-8") as my_file:
        print(my_file.read().rstrip())
