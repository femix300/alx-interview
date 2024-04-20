#!/usr/bin/python3
'''N queens'''
import sys
from typing import List

args = sys.argv

if len(args) < 2:
    print('Usage: nqueens N')
    sys.exit(1)

if not args[1].isdecimal():
    print('N must be a number')
    sys.exit(1)

args[1] = int(args[1])

if args[1] < 4:
    print('N must be at least 4')
    sys.exit(1)


def nqueens(n: int) -> List[List[int]]:
    '''finds spots where a queen can be placed'''
    col = set()
    posDiag = set()
    negDiag = set()

    res = []

    def backtrack(r, board):
        if r == n:
            res.append(board)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)

            new_board = board + [[r, c]]
            backtrack(r + 1, new_board)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)

    backtrack(0, [])

    return res


solutions = nqueens(args[1])

for solution in solutions:
    print(solution)
