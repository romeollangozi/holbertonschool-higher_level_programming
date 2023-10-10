#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n_elem = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            n_elem += 1
        except IndexError:
            print()
            return n_elem
            break
    print()
    return n_elem
