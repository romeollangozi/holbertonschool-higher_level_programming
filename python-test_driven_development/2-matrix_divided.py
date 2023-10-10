#!/usr/bin/python3

'''

    Simple module to practice doctest module
    for automating testing

'''


def matrix_divided(matrix, div):
    error = "matrix must be a matrix (list of lists) of integers/floats"
    '''

        Function that returns a new matrix with
        elemnts divided by div argument
    '''

    if type(matrix) is not list:
        raise TypeError(error)
    row_length = len(matrix[0])
    for element in matrix:
        if type(element) is not list:
            raise TypeError(error)
            break
        elif len(element) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for integer in element:
            if type(integer) not in [int, float]:
                raise TypeError(error)
                break
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
