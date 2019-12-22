import sys
from collections import defaultdict
import random

import numpy as np

from day08 import black, white
from day09 import split_op, n_args, write_instrs

def prog(l, in_):
    res = defaultdict(int, enumerate(map(int, l.split(','))))
    out = None
    i = 0 # instruction counter
    r = 0 # relative base
    iterations = 0

    while True:
        iterations += 1
        # print("Iteration:", iterations)
        instr, modes = split_op(res[i])
        if instr == '99': # Halt
            break

        args = []
        for j, m in enumerate(modes):
            if m[0] == '0':
                args.append(res[res[i + j + 1]])
            elif m[0] == '1':
                args.append(res[i + j + 1])
            elif m[0] == '2':
                args.append(res[res[i + j + 1] + r])
            else:
                raise ValueError("Unrecognized mode %s" % m[0])
        if instr in write_instrs:
            addr = res[i + n_args[instr]]
            if modes[-1] == '2':
                addr += r

        assert len(args) == n_args[instr], (instr, args)

        if instr == '01': # Add
            res[addr] = args[0] + args[1]
            i += 4
        elif instr == '02': # Mul
            res[addr] = args[0] * args[1]
            i += 4
        elif instr == '03': # Input
            res[addr] = in_.pop(0)
            i += 2
        elif instr == '04': # Output
            out = args[0]
            yield out
            i += 2
        elif instr == '05': # Jump if nonzero
            if args[0] != 0:
                i = args[1]
            else:
                i += 3
        elif instr == '06': # Jump if zero
            if args[0] == 0:
                i = args[1]
            else:
                i += 3
        elif instr == '07': # Less than
            res[addr] = int(args[0] < args[1])
            i += 4
        elif instr == '08': # Equals
            res[addr] = int(args[0] == args[1])
            i += 4
        elif instr == '09': # Adjust relative base
            r += args[0]
            i += 2
        else:
            raise ValueError("bad instruction %s" % i)

def compute_prog(input, p=None):
    in_ = []
    p = p or prog(input, in_)
    A = defaultdict(int)
    A[0, 0] # Initialize
    score = 0
    paddlex = paddley = ballx0 = ballx1 = bally = -1
    moves = 0
    while True:
        try:
            # print_game(A, score)
            x = next(p)
            y = next(p)
            tile_id = next(p)
            if x == -1:
                score = tile_id
            else:
                A[x, y] = tile_id
            if tile_id == 3: # Paddle
                paddlex = x
                paddley = y
            if tile_id == 4: # Ball
                ballx0, ballx1 = ballx1, x
                bally = y
            if not in_ and tile_id == 4:
                moves += 1
                if paddlex > ballx1:
                    in_.append(-1)
                elif paddlex < ballx1:
                    in_.append(1)
                # elif ballx1 > ballx0:
                #     in_.append(1)
                # elif ballx1 < ballx0:
                #     in_.append(-1)
                elif bally == paddley - 1:
                    in_.append(random.choice([-1, 0, 1]))
                    print("Random")
                else:
                    in_.append(0)
                print("Paddle at", paddlex, paddley)
                print("Ball was at", ballx0)
                print("Ball at", ballx1, bally)
                print("Sending input", in_[0])
                print_game(A, score)
        except StopIteration:
            print("Game Over in", moves, "moves")
            print_game(A, score)
            return A, score

empty = white
wall = black
block = '▒'
paddle = '━'
ball = 'o'

D = {
    0: empty,
    1: wall,
    2: block,
    3: paddle,
    4: ball,
}

def toarray(A):
    shape = tuple(i + 2 for i in max(A))
    B = np.zeros(shape, dtype=np.int64)
    for x, y in A:
        B[x, y] = A[x, y]
    return B

def print_game(A, score):
    B = toarray(A)
    print("Score:", score)
    # paddle = None
    S = ''
    for y in range(B.shape[1]):
        for x in range(B.shape[0]):
            S += D[B[x, y]]
            # if B[x, y] == 3:
            #     paddle = x, y
        S += '\n'
    print(S)
    # print("Paddle was at", paddle)
    import time
    time.sleep(0.1)

with open('day13-input') as f:
    input = f.read()

if __name__ == '__main__':
    if sys.argv[1:] == ['1']:
        print("Day 13 Part 1")
        A, score = compute_prog(input)
        print(np.sum(toarray(A) == 2))
    elif sys.argv[1:] == ['2']:
        print("Day 13 Part 2")
        input = '2' + input[1:]
        A = compute_prog(input)
    else:
        sys.exit("Error: must run 'python day13.py 1' or 'python day13.py 2'.")
