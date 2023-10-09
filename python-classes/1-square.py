#!/usr/bin/python3
'''
Simple python file for createing a Square class
and its initiliazation with one private instance attribute
'''


class Square:
    '''
    Square class
    '''

    def __init__(self, size):
        '''
        Init method for square instances
        Args:
            size (int): Size of the square
        '''

        self.__size = size
