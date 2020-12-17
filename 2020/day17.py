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
def parse(text, n, extra_dims=1):
    A = np.array(text.strip().split(), 'c')
    i, j = A.shape
    # print(A)
    B = np.full((i + 2*n + 1, j + 2*n + 1) + (2*n + 1,)*extra_dims, '.', dtype='c')
    B[(slice(n, i + n), slice(n, j + n)) + (n,)*extra_dims] = A
    return B

def neighbors(*indices):
    for offsets in product((-1, 0, 1), repeat=len(indices)):
        if all(o == 0 for o in offsets):
            continue
        yield tuple([i + o for i, o in zip(indices, offsets)])

def cycle(A, extra_dims=1):
    if extra_dims not in [1, 2]:
        raise ValueError("extra_dims must be 1 or 2")
    B = A.copy()
    if extra_dims == 2:
        I, J, K, L = A.shape
    else:
        I, J, K = A.shape
        L = 1
    for i in range(I):
        for j in range(J):
            for k in range(K):
                for l in range(L):
                    idx = (i, j, k) if extra_dims == 1 else (i, j, k, l)
                    active = (A[idx] == b'#')
                    active_neighbors = 0
                    for newidx in neighbors(*idx):
                        if any(i >= s or i < 0 for i, s in zip(newidx, A.shape)):
                            continue
                        if A[newidx] == b'#':
                            active_neighbors += 1
                    if active and active_neighbors not in [2, 3]:
                        B[idx] = b'.'
                    elif not active and active_neighbors == 3:
                        B[idx] = b'#'
    return B

def run(A, n, extra_dims=1):
    for i in range(n):
        A = cycle(A, extra_dims=extra_dims)
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

print("Part 2")
print("Test input")
test_A_4 = parse(test_input, n, extra_dims=2)
test_B_4 = run(test_A_4, n, extra_dims=2)
print(np.sum(test_B_4 == b'#'))

print("Puzzle input")
A_4 = parse(input, n, extra_dims=2)
B_4 = run(A_4, n, extra_dims=2)
print(np.sum(B_4 == b'#'))
