#!/usr/bin/python3

'''
Python simple module
for demonstarative purpose
'''


def is_same_class(obj, a_class):
    '''
    Function that returns True if an object is an instance
    of a_class
    '''
    return obj.__class__.__name__ == a_class.__name__
