#!/usr/bin/python3

def max_integer(my_list=[]):
    max_number = 0
    if len(my_list) == 0:
        return None
    for number in my_list:
        if number > max_number:
            max_number = number
    return max_number
