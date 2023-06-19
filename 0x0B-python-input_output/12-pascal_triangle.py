#!/usr/bin/python3
"""
Module contains the function pascal_triangle
Returns a list of integers rep the Pascal's integers.
"""


def pascal_triangle(n):
    """returns list of ints rep the triangle."""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for t in range(len(tri) - 1):
            tmp.append(1)
            triangles.append(tmp)
        return triangles
