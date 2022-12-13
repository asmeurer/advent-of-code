test_input = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

input = open('day12_input').read()

import numpy as np
# from numba import njit

def parse_input(data):
    a = np.array([[ord(i) - ord('a') for i in line] for line in data.strip().splitlines()])
    start = np.where(a == ord("S") - ord('a'))
    a[start] = 0
    end = np.where(a == ord("E") - ord('a'))
    a[end] = ord('z') - ord('a')
    return a, where_to_idx(start), where_to_idx(end)

def where_to_idx(w):
    return (w[0][0], w[1][0])

def neighbors(idx, shape):
    i, j = idx
    if i > 0:
        yield i - 1, j
    if i < shape[0] - 1:
        yield i + 1, j
    if j > 0:
        yield i, j - 1
    if j < shape[1] - 1:
        yield i, j + 1

# @njit
def argmin_dist(dist, Q):
    min_val = float('inf')
    min_idx = (0, 0)
    for i, j in np.ndindex(*dist.shape):
        if Q[i, j]:
            m = dist[i, j]
            if m <= min_val:
                min_val = m
                min_idx = (i, j)
    assert min_idx != (-1, -1)
    return min_idx


def dijkstra(a, start, end):
    dist = np.full_like(a, float('inf'), dtype=float)
    dist[start] = 0.

    Q = np.full_like(a, True, dtype=bool)
    while np.any(Q):
        u = argmin_dist(dist, Q)
        if u == end:
            return dist
        Q[u] = False

        for v in neighbors(u, a.shape):
            if a[v] > a[u] + 1:
                # More than one step up, not really a neighbor
                continue
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
    return dist

def part1(a, start, end):
    dist = dijkstra(a, start, end)
    return int(dist[end])

def part2(a, end):
    paths = []
    for start in np.ndindex(*a.shape):
        if a[start] == 0:
            try:
                paths.append(part1(a, start, end))
            except OverflowError:
                pass
    return min(paths)

print("Day 12")
print("Part 1")
print("Test input")
test_a, test_start, test_end = parse_input(test_input)
print(test_a)
print(test_start)
print(test_end)
print(dijkstra(test_a, test_start, test_end))
print(part1(test_a, test_start, test_end))
print("Puzzle input")
a, start, end = parse_input(input)
# print(dijkstra(a, start, end))
print(part1(a, start, end))
print("Part 2")
print("Test input")
print(part2(test_a, test_end))
print("Puzzle input")
print(part2(a, end))
