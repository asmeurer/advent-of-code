import time

import numpy as np

from day13 import prog

def run(input, in_=None, print_=False):
    in_ = in_ or []
    p = prog(input, in_)
    out = ''
    while True:
        try:
            out += chr(next(p))
            if print_:
                print(out[-1], end='')
                if out[-2:] == '\n\n':
                    time.sleep(0.1)
        except StopIteration:
            return out

def toarray(out):
    lines = out.strip().splitlines()
    A = np.zeros((len(lines), len(lines[0])))
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                A[i, j] = 1
            elif lines[i][j] in '<>^v':
                A[i, j] = 2
            elif lines[i][j] == '.':
                pass
            else:
                raise ValueError("Unexpected character: %s" % lines[i][j])
    return A

def find_intersections(A):
    intersections = []
    for i, j in np.ndindex(A.shape):
        if A[i][j] == 1:
            if i > 0 and A[i-1][j] == 0:
                continue
            if i < A.shape[0] - 1 and A[i + 1][j] == 0:
                continue
            if j > 0 and A[i][j-1] == 0:
                continue
            if j < A.shape[1] - 1 and A[i][j + 1] == 0:
                continue
            intersections.append((i, j))
    return intersections

def alignment(intersections):
    return sum(i*j for i, j in intersections)

with open('day17-input') as f:
    input = f.read()

test_input = """
..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..
"""

main = 'A                B             B             A                B             C                A                C                B             C'
path = 'L,4,L,6,L,8,L,12 L,8,R,12,L,12 L,8,R,12,L,12 L,4,L,6,L,8,L,12 L,8,R,12,L,12 R,12,L,6,L,6,L,8 L,4,L,6,L,8,L,12 R,12,L,6,L,6,L,8 L,8,R,12,L,12 R,12,L,6,L,6,L,8'
_main = ','.join(main.split())
A = path.split()[0]
B = path.split()[1]
C = path.split()[-1]

assert len(A) <= 20
assert len(B) <= 20
assert len(C) <= 20

def main():
    print("Day 17 part 1 test input")
    Arr = toarray(test_input)
    intersections = find_intersections(Arr)
    print("Should return 76")
    print(alignment(intersections))

    print("Day 17 part 1 test input")
    out = run(input)
    print(out)
    Arr = toarray(out)
    intersections = find_intersections(Arr)
    print(alignment(intersections))

    print("Day 17 part 2")
    input2 = '2' + input[1:]
    in_ = []
    for cmd in [_main, A, B, C]:
        for c in cmd:
            in_.append(ord(c))
        in_.append(ord('\n'))
    in_.extend([ord('y'), ord('\n')])

    print("Input:", ''.join([chr(i) for i in in_]))
    out = run(input2, in_, print_=True)
    print()
    print(ord(out[-1]))

if __name__ == '__main__':
    main()
