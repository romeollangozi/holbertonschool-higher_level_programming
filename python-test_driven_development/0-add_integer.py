#!/usr/bin/python3

'''

 Simple module to test doctest module for test autmoatizaton
 for the below function which adds two integers
 this is only for learning puproses
'''


def add_integer(a, b=98):

    '''
    Simple function that adds two integers

    Args:
        a (int) : an integer value
        b (int) : an integer value set to 98 by default

    Return:
        Addition of the two arguments

    Raises:
        TypeError: if a or b is not a integer or if function is called
                   with less than or more than 2 arguments
    '''

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
