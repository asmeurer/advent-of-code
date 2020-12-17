test_input = """
.#.
..#
###
"""

input = """
.###..#.
##.##...
....#.#.
#..#.###
...#...#
##.#...#
#..##.##
#.......
"""

from itertools import product

import numpy as np

# From 2019/day10.py
def parse(text, n):
    A = np.array(text.strip().split(), 'c')
    i, j = A.shape
    # print(A)
    B = np.full((i + 2*n + 1, j + 2*n + 1, 2*n + 1), '.', dtype='c')
    B[n:i+n, n:j+n, n] = A
    return B

def neighbors(i, j, k):
    for a, b, c in product((-1, 0, 1), repeat=3):
        if a == b == c == 0:
            continue
        yield (i + a, j + b, k + c)

def cycle(A):
    B = A.copy()
    I, J, K = A.shape
    for i in range(I):
        for j in range(J):
            for k in range(K):
                active = (A[i, j, k] == b'#')
                active_neighbors = 0
                for a, b, c in neighbors(i, j, k):
                    if a >= I or a < 0 or b >= J or b < 0 or c >= K or c < 0:
                        continue
                    if A[a, b, c] == b'#':
                        active_neighbors += 1
                if active and active_neighbors not in [2, 3]:
                    B[i, j, k] = b'.'
                elif not active and active_neighbors == 3:
                    B[i, j, k] = b'#'
    return B

def run(A, n):
    for i in range(n):
        A = cycle(A)
    return A

print("Day 17")
print("Part 1")
print("Test input")
n = 6
test_A = parse(test_input, n)
print("Initial")
print(test_A)
print(test_A.shape)
print(test_A[..., 0])
print("1 cycles")
test_A1 = cycle(test_A)
print(test_A1[..., n-1])
print(test_A1[..., n])
print(test_A1[..., n+1])
print("2 cycles")
test_A2 = cycle(test_A1)
print(test_A2[..., n-2])
print(test_A2[..., n-1])
print(test_A2[..., n])
print(test_A2[..., n+1])
print(test_A2[..., n+2])

test_B = run(test_A, n)
print(np.sum(test_B == b'#'))

print("Puzzle input")
A = parse(input, n)
B = run(A, n)
print(np.sum(B == b'#'))
