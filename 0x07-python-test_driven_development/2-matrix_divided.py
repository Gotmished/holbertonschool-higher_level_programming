#!/usr/bin/python3
"""
The "2-matrix_divided" module, with one function:

matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by a number and returns the new matrix
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_length = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        row_length.append(len(row))
        if not all(len_element == row_length[0] for len_element in row_length):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    div_matrix = [[round(number / div, 2) for number in row] for row in matrix]
    return div_matrix
