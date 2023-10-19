#!/usr/bin/python3
'''
Module for demostrative purposes
'''


import json


def class_to_json(obj):
    '''
    Function to convert an object
    as a json string
    '''
    return json.loads(json.dumps(obj.__dict__))
