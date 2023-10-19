#!/usr/bin/python3
'''
Module for demostrative purposes
'''


class Student:
    '''
    Simple class Student
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Initialization method for Stduent objects
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Function to returns a dictionary
        represantation of Student object
        '''
        if type(attrs) is list and all(type(thing) is str for thing in attrs):
            new_dict = {}
            for attribute in attrs:
                if attribute in self.__dict__.keys():
                    new_dict[attribute] = self.__dict__[attribute]
            return new_dict
        return self.__dict__
