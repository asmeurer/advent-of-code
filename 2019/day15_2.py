from collections import defaultdict
import sys

import numpy as np

from day13 import prog

from day15_1 import moves, print_board, input, create_tree

def run(input, p=None, max_iter=sys.maxsize, print_=False):
    in_ = []
    p = p or prog(input, in_)
    A = defaultdict(int)
    A[0, 0] = -2 # Initialize

    pos = np.array([0, 0])

    rotate_clockwise = {1: 4, 4: 2, 2: 3, 3: 1}
    rotate_counterclockwise = {1: 3, 3: 2, 2: 4, 4: 1}
    move = 1
    dir = 4

    for i in range(max_iter):
        try:
            if not in_:
                in_.append(move)
            status = next(p)
            if status == 0:
                # Hit a wall
                A[tuple(pos + moves[move])] = 1
                dir = rotate_clockwise[dir]
                move = dir
            elif status == 1:
                # Moved
                pos += moves[move]
                if tuple(pos) != (0, 0):
                    A[tuple(pos)] = -1
                move = rotate_counterclockwise[dir]
                dir = move
            elif status == 2:
                # Moved and found oxygen
                pos += moves[move]
                A[tuple(pos)] = 2
                dir = move
                move = rotate_counterclockwise[dir]
            if print_:
                print_board(A, pos)
            if tuple(pos) == (0, 0) and i > 4:
                return A, pos
        except StopIteration:
            return A, pos

    raise RuntimeError("Did not find a solution")


def bfs(tree, path):
    for item in tree[path[-1]]:
        yield from bfs(tree, path + [item])
        yield path + [item]

def main():
    A, pos = run(input, print_=False)
    print_board(A, pos)
    oxygen = [i for i in A if A[i] == 2][0]
    tree = create_tree(A, oxygen)
    for i in bfs(tree, [oxygen]):
        print(i)

if __name__ == '__main__':
    main()
