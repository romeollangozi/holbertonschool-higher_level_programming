#!/usr/bin/python3
'''

Simple python file for createing a Square class
and its initiliazation with one private instance attribute
'''


class Square:
    '''

    Square class
    '''

    def __init__(self, size=0):
        '''

        Init method for square instances
        Args:
            size (int): Size of the square
        '''
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    '''

    Public instance method to calculate the area of the instance square
    '''

    def area(self):
        return self.__size ** 2
