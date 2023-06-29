#!/usr/bin/python3
"""
Defines a function matrix_divided(matrix, div)
Function devides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """returns a divided matrix rounded to 2 decimals."""
    import decimal
    error_mssg = "matrix must be a matrix (list of lists) of integers/float"
    if type(matrix) is not list:
        raise TypeError(error_mmsg)
    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_mmsg)
        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_mssg)
        row_count += 1
    if len(set(len_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
