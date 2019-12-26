import numpy as np

from day13 import prog

def run(input, p=None):
    in_ = []
    p = p or prog(input, in_)
    out = ''
    while True:
        try:
            out += chr(next(p))
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

def main():
    print("Day 17 part 1 test input")
    A = toarray(test_input)
    intersections = find_intersections(A)
    print("Should return 76")
    print(alignment(intersections))

    print("Day 17 part 1 test input")
    out = run(input)
    print(out)
    A = toarray(out)
    intersections = find_intersections(A)
    print(alignment(intersections))


if __name__ == '__main__':
    main()
