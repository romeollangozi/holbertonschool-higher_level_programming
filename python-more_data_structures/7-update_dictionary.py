#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if a_dictionary != None or key != None or value != None:
        a_dictionary[key] = value
        return a_dictionary
