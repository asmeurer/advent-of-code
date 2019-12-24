import random
from collections import defaultdict
import sys

import numpy as np

from day13 import prog, empty, wall, block

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
                A[tuple(pos + moves[move])] = -1
                pos += moves[move]
            elif status == 2:
                # Moved and found oxygen
                A[tuple(pos + moves[move])] = 2
                return A, pos

            if print_:
                print_board(A, pos)
        except StopIteration:
            return A, pos

    raise RuntimeError("Did not find a solution")

# From https://timvieira.github.io/blog/post/2019/09/06/the-restart-acceleration-trick-a-cure-for-the-heavy-tail-of-wasted-time/
def luby():
    def h(k):
        if k == 0:
            yield 1
        else:
            for j in range(k):
                yield from h(j)
            yield 2 ** k

    i = 0
    while True:
        yield from h(i)
        i += 1

moves = {
    1: np.array([0, -1]), # north
    2: np.array([0, 1]), # south
    3: np.array([1, 0]), # west
    4: np.array([-1, 0]), # east
}

bot = '🤖'
oxygen = 'O₂'
start = 'ⓧ '

D = {
    -2: start,   # Start
    -1: 2*block, # Discovered empty
    0: 2*empty,  # Undiscovered
    1: 2*wall,   # Wall
    2: oxygen,   # Oxygen
}

def print_board(A, pos):
    min_x = min(list(A) + [pos], key=lambda i: i[0])[0]
    max_x = max(list(A) + [pos], key=lambda i: i[0])[0]
    min_y = min(list(A) + [pos], key=lambda i: i[1])[1]
    max_y = max(list(A) + [pos], key=lambda i: i[1])[1]
    S = ''
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) == tuple(pos):
                S += bot
            else:
                S += D[A[x, y]]
        S += '\n'
    print(S)
    print('-------------------')
    # import time
    # time.sleep(0.1)

def retry(input):
    for r in luby():
        try:
            iters = r*500
            print("Trying with", iters, "max iterations")
            A, pos = run(input, max_iter=iters, print_=False)
            return A, pos
        except RuntimeError:
            pass

def create_tree(A):
    tree = defaultdict(set)
    # Make sure (0, 0) is included as the base
    add_to_tree(A, tree, (0, 0))

    for pos in A:
        add_to_tree(A, tree, pos)

    return tree

def add_to_tree(A, tree, pos):
    for move in moves.values():
        pos2 = tuple(np.array(pos) + move)
        if pos2 in A and A[pos2] in [-1, 2] and pos not in tree[pos2]:
            tree[pos].add(pos2)

def dfs(tree, path):
    for item in tree[path[-1]]:
        yield path + [item]
        yield from dfs(tree, path + [item])

with open('day15-input') as f:
    input = f.read()

def main():
    A, pos = retry(input)
    print_board(A, pos)
    tree = create_tree(A)
    oxygen = [i for i in A if A[i] == 2][0]
    for path in dfs(tree, [(0, 0)]):
        if path[-1] == oxygen:
            # print(path)
            print(len(path) - 1, "moves")
            break
    else:
        print("Error: couldn't find path")


if __name__ == '__main__':
    main()
