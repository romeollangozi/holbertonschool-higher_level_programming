#!/usr/bin/python3

'''
Python simple module
for demonstarative purpose
'''


def inherits_from(obj, a_class):
    '''
    Function that returns True if an object is an instance
    of a_class
    '''
    return isinstance(obj, a_class) and type(obj) is not a_class
