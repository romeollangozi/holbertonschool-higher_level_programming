#!/usr/bin/python3

'''

    Module to test doctest module with a simple function which
    concatenates two strings together
'''


def say_my_name(first_name, last_name=""):

    '''

    Function who takes two string as arguments
    and prints them in a sentence
    '''

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
