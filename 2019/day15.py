from random import choice
from collections import defaultdict

import numpy as np

from day13 import prog, empty, wall, toarray

def run(input, p=None):
    in_ = []
    p = p or prog(input, in_)
    A = defaultdict(int)
    A[0, 0] # Initialize

    pos = np.array([0, 0])

    while True:
        try:
            if not _in:
                move = random.choice(moves)
                in_.append(move)
            status = next(p)
            if status == 0:
                # Hit a wall
                A[tuple(pos + moves[move])] = 1
            elif status == 1:
                # Moved
                A[tuple(pos + moves[move])] = 0
                pos += moves[move]
            elif status == 2:
                # Moved and found oxygen
                A[tuple(pos + moves[move])] = 2
                pos += moves[move]
                return A

            print_board(A, pos)
        except StopIteration:
            return A

moves = {
    1: np.array([0, -1]), # north
    2: np.array([0, 1]), # south
    3: np.array([1, 0]), # west
    4: np.array([-1, 0]), # east
}

bot = '🤖'
oxygen = 'O₂'
D = {
    1: wall,
    0: empty,
    2: oxygen,
}

def print_board(A, pos):
    B = toarray(A)
    S = ''
    for y in range(B.shape[1]):
        for x in range(B.shape[0]):
            if (x, y) == tuple(pos):
                S += bot
            else:
                S += 2*D[B[x, y]]
        S += '\n'
    print(S)
    import time
    time.sleep(0.01)

with open('day15-input') as f:
    input = f.read()

if __name__ == '__main__':
    pass
