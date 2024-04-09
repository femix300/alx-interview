#!/usr/bin/python3
"""UTF-8 Validation.
"""
from typing import List


def count_ones(num):
    '''
    Counts the number of 1's in a binary number
    '''
    count = 0
    for i in range(7, -1, -1):
        if num & (1 << i):
            count += 1
        else:
            break
    return count


def validUTF8(data: List[int]) -> bool:
    '''
    Checks if a given set of data is valid utf-8 encoding
    '''
    count = 0
    for d in data:
        if not count:
            count = count_ones(d)

            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
            count -= 1
        else:
            count -= 1
            if count_ones(d) != 1:
                return False
    return count == 0
