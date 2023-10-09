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
        self.size = size

    '''

    Property setter for attribute size
    '''

    @property
    def size(self):
        return self.__size

    '''

    Property decorator for setting size attribute
    '''

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    '''

    Public instance method to calculate the area of the instance square
    '''

    def area(self):
        return self.size ** 2
