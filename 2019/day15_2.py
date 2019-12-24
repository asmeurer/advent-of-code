import random
from collections import defaultdict
import sys

import numpy as np

from day13 import prog

from day15_1 import moves, print_board, luby, input, create_tree

def run(input, p=None, max_iter=sys.maxsize, print_=False):
    in_ = []
    p = p or prog(input, in_)
    A = defaultdict(int)
    A[0, 0] = -2 # Initialize

    pos = np.array([0, 0])

    move = None

    for i in range(max_iter):
        try:
            if not in_:
                possible_moves = []
                for move in moves:
                    if A[tuple(pos + moves[move])] == 0:
                        possible_moves.append(move)
                if not possible_moves:
                    possible_moves = list(moves)
                move  = random.choice(possible_moves)
                in_.append(move)
            status = next(p)
            if status == 0:
                # Hit a wall
                A[tuple(pos + moves[move])] = 1
            elif status == 1:
                # Moved
                pos += moves[move]
                if tuple(pos) != (0, 0):
                    A[tuple(pos)] = -1
            elif status == 2:
                # Moved and found oxygen
                pos += moves[move]
                A[tuple(pos)] = 2
            if print_ and i % 100 == 0:
                print_board(A, pos)
            if full(A):
                return A, pos
        except StopIteration:
            return A, pos

    raise RuntimeError("Did not find a solution")

def full(A):
    min_x = min(list(A), key=lambda i: i[0])[0]
    max_x = max(list(A), key=lambda i: i[0])[0]
    min_y = min(list(A), key=lambda i: i[1])[1]
    max_y = max(list(A), key=lambda i: i[1])[1]
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if A[x, y] == 0:
                # Ignore spaces that are completely surrounded by wall
                for move in moves.values():
                    x2, y2 = tuple(np.array([x, y]) + move)
                    if x2 < min_x or x2 > max_x or y2 < min_y or y2 > max_y:
                        continue
                    if A[x2, y2] != 1:
                        return False
                return False
    return True

def main():
    A, pos = run(input, print_=True)
    print_board(A, pos)
    oxygen = [i for i in A if A[i] == 2][0]
    tree = create_tree(A, oxygen)
    print(tree)

if __name__ == '__main__':
    main()
