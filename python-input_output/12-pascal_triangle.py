#!/usr/bin/python3
'''
Module for demostratve purposes
'''


def pascal_triangle(n):
    '''
    Function to print pascal triangle
    '''
    if n <= 0:
        return []
    if n <= 1:
        return [[1]]
    triangle = pascal_triangle(n - 1)
    prev_row = triangle[-1]
    new_row = [1]
    for i in range(len(prev_row) - 1):
        new_row.append(prev_row[i] + prev_row[i + 1])
    new_row.append(1)
    triangle.append(new_row)
    return triangle
