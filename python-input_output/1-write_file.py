#!/usr/bin/python3

'''
Python module for demostrative purpose
'''


def write_file(filename="", text=""):
    '''
    Simple function for reading specified file
    '''

    with open(filename, 'w', encoding="utf-8") as my_file:
        n_bytes = my_file.write(text)

    return n_bytes
