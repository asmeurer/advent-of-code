from collections import defaultdict

import numpy as np

from day8 import black, white, inverse
from day9 import split_op, n_args, write_instrs

def prog(l, in_):
    res = defaultdict(int, enumerate(map(int, l.split(','))))
    out = None
    i = 0 # instruction counter
    r = 0 # relative base

    while True:
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
            res[addr] = yield from in_
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

def compute_prog(input, shape=(10, 10), p=None):
    in_ = []
    p = p or prog(input, in_)
    X = np.array([shape[0]//2, shape[1]//2])
    dir = np.array([0, 1])
    # 0 = uninitialized black
    # 1 = colored black
    # -1 = colored white
    A = np.zeros(shape, dtype=np.int64)
    while True:
        try:
            print_block(A, X, dir)
            if np.any(X < 0) or np.any(X >= shape):
                raise ValueError("The shape is too small (%s)" % X)
            in_.append(0 if A[tuple(X)] in [0, 1] else 1)
            color = next(p)
            dir_change = next(p)
            if color is None or dir_change is None:
                return A
            A[tuple(X)] = 1 if color == 0 else -1
            inc(dir_change, dir, X)
            # from time import sleep
            # sleep(1)
            print()
        except StopIteration:
            return A

def print_block(A, X, dir):
    dirchar = {
        (1, 0): '>',
        (-1, 0): '<',
        (0, 1): '^',
        (0, -1): 'v',
    }
    for y in range(A.shape[0] - 1, -1, -1):
        for x in range(A.shape[1]):
            entry = A[x, y]
            if (x, y) == tuple(X):
                if entry in [0, 1]:
                    print(inverse(dirchar[tuple(dir)]), end='')
                else:
                    print(dirchar[tuple(dir)], end='')
            elif entry in [0, 1]:
                print(black, end='')
            else:
                print(white, end='')
        print()

def inc(o, dir, X):
    R = np.array([[0, -1], [1, 0]]) # Rotation matrix for 90 degrees counterclockwise
    if o == 0:
        dir[:] = R @ dir
    elif o == 1:
        dir[:] = -R @ dir
    else:
        raise RuntimeError("Unexpected output % s" % o)
    X += dir

def test_prog():
    for i in [1, 0,
              0, 0,
              1, 0,
              1, 0,
              0, 1,
              1, 0,
              1, 0,
              ]:
        yield i

input = '3,8,1005,8,335,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,28,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,51,1006,0,82,1006,0,56,1,1107,0,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,83,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,104,1006,0,58,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,129,1006,0,54,1006,0,50,1006,0,31,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,161,2,101,14,10,1006,0,43,1006,0,77,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,193,2,101,12,10,2,109,18,10,1,1009,13,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,226,1,1103,1,10,1,1007,16,10,1,3,4,10,1006,0,88,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,263,1006,0,50,2,1108,17,10,1006,0,36,1,9,8,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,300,1006,0,22,2,106,2,10,2,1001,19,10,1,3,1,10,101,1,9,9,1007,9,925,10,1005,10,15,99,109,657,104,0,104,1,21101,0,937268454156,1,21102,1,352,0,1106,0,456,21101,0,666538713748,1,21102,363,1,0,1105,1,456,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,3316845608,0,1,21102,1,410,0,1105,1,456,21101,0,209475103911,1,21101,421,0,0,1106,0,456,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,984353603944,1,21101,444,0,0,1105,1,456,21102,1,988220752232,1,21102,1,455,0,1106,0,456,99,109,2,22101,0,-1,1,21102,40,1,2,21101,487,0,3,21101,0,477,0,1106,0,520,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,482,483,498,4,0,1001,482,1,482,108,4,482,10,1006,10,514,1102,0,1,482,109,-2,2105,1,0,0,109,4,2101,0,-1,519,1207,-3,0,10,1006,10,537,21101,0,0,-3,22101,0,-3,1,22101,0,-2,2,21102,1,1,3,21101,556,0,0,1106,0,561,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,584,2207,-4,-2,10,1006,10,584,21201,-4,0,-4,1106,0,652,22101,0,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,0,603,0,1105,1,561,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,622,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,644,21201,-1,0,1,21101,644,0,0,105,1,519,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0'

def main():
    A = compute_prog(input, shape=(10, 10), p=test_prog())
    print(np.sum(abs(A)))

    return

    A = compute_prog(input, shape=(20, 20))
    print(np.sum(abs(A)))

if __name__ == '__main__':
    main()
