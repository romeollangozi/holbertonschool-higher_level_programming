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

    with open(filename, 'r') as my_file:
        return json.loads(my_file.read())
