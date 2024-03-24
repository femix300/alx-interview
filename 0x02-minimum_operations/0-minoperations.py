#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    '''
    calculates the fewest number of operations needed
    to result in exactly n H characters
    '''

    operations = 0
    divider = 2

    while n > 1:
        if n % divider == 0:
            n = n / divider
            operations += divider
        else:
            divider += 1
    return operations
