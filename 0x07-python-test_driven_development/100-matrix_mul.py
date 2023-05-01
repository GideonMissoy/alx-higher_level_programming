#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """Multiply two matrices"""

    if type(m_a) != list:
        raise TypeError('m_a must be a list')

    if type(m_b) != list:
        raise TypeError('m_b must be a list')

    num_colm1 = 0
    num_row2 = 0

    # Check first matrix m_a
    if m_a == []:
        raise ValueError("m_a can't be empty")

    for row1 in m_a:
        if type(row1) != list:
            raise TypeError("m_a must be a list of lists")

        len1 = len(m_a[0])

        if row1 == []:
            raise ValueError("m_a can't be empty")

        if len1 != len(row1):
            raise TypeError("each row of m_a must be of the same size")

        num_colm1 = len(row1)

        for colm1 in row1:
            if type(colm1) != int and type(colm1) != float:
                raise TypeError("m_a should contain only integers or floats")

    # Check second matrix m_b
    if m_b == []:
        raise ValueError("m_b can't be empty")

    for row2 in m_b:
        if type(row2) != list:
            raise TypeError("m_b must be a list of lists")

        len2 = len(m_b[0])

        if row2 == []:
            raise ValueError("m_b can't be empty")

        if len2 != len(row2):
            raise TypeError("each row of m_b must be of the same size")

        num_row2 += 1

        for colm2 in row2:
            if type(colm2) != int and type(colm2) != float:
                raise TypeError("m_b should contain only integers or floats")

    if num_colm1 != num_row2:
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply matrices
    mul_matrix = []

    for row_1 in m_a:
        ln = 0
        l_row = []

        while ln < len(m_b[0]):
            result = 0
            c = 0

            for colm_1 in row_1:
                result += colm_1 * m_b[c][ln]
                c += 1

            l_row.append(result)
            ln += 1

        mul_matrix.append(l_row)

    return mul_matrix
