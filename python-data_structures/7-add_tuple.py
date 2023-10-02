#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_first = 0 if len(tuple_a) < 1 else tuple_a[0]
    a_second = 0 if len(tuple_a) < 2 else tuple_a[1]
    b_first = 0 if len(tuple_b) < 1 else tuple_b[0]
    b_second = 0 if len(tuple_b) < 2 else tuple_b[1]
    return (a_first + b_first, a_second + b_second)
