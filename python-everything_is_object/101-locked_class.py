#!/usr/bin/python3
'''
Module for demostrative purposes
'''


class LockedClass:
    '''
    Class example for demostrative purposes
    '''
    __slots__ = ['first_name']

    def __init__(self, name=""):
        '''
        Init function for LockedClass object instances
        '''
        self.first_name = name
