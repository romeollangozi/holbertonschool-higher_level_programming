#!/usr/bin/python3
'''
Module for demostrative purposes
'''


import json


def load_from_json_file(filename):
    '''
    Function to convert an object
    as a json string
    '''

    with open(filename, 'w', encoding="utf-8") as my_file:
        return json.load(my_file)
