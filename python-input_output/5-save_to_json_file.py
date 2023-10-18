#!/usr/bin/python3
'''
Module for demostrative purposes
'''


import json


def save_to_json_file(my_obj, filename):
    '''
    Function to convert an object
    as a json string
    '''

    with open(filename, 'w', encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
