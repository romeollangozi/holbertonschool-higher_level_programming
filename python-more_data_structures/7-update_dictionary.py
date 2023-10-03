#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if a_dictionary or key or value is not None:
        a_dictionary[key] = value
        return a_dictionary
