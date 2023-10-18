#!/usr/bin/python3
'''
Python simple module
for demonstarative purpose
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
    Class that inherits from list class
    '''
    def __init__(self, size):
        '''
        Init function for Square class
        '''
        Rectangle.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        '''
        Instance method to calculate area
        '''
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
