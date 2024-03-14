#!/usr/bin/python3

"""A python program that implements the pascal's triangle"""


def pascal_triangle(n):
    """Implements the pascal's triangle"""

    if n <= 0:
        return []
    res = [[1]]

    for i in range(n-1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(temp) - 1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res
