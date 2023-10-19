#!/usr/bin/python3
'''
Module for demostrative purposes
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Function that inserts a line of text to a file
    after each line containing a specific string
    '''

    with open(filename, "r+") as my_file:
        lines = my_file.readlines()
        for line in lines:
            if search_string in line:
                lines.insert(lines.index(line) + 1, new_string)
        with open(filename, "w") as new_file:
            new_file.write(''.join(lines))
