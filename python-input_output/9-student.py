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

    def to_json(self):
        '''
        Function to returns a dictionary
        represantation of Student object
        '''

        return self.__dict__
