#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None:
        max_val = max(a_dictionary, default=None)
        return max_val
    else:
        return None
