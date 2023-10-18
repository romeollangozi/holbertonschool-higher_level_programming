#!/usr/bin/python3

'''
Python module for demostrative purpose
'''


def append_write(filename="", text=""):
    '''
    Simple function for reading specified file
    '''

    with open(filename, 'a', encoding="utf-8") as my_file:
        n_bytes = my_file.write(text)

    return n_bytes
