#!/usr/bin/python3
'''
Python simple module
for demonstarative purpose
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Class that inherits from list class
    '''
    def __init__(self, width, height):
        '''
        Init function for Rectangle class
        '''
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
