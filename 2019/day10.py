import numpy as np

from math import gcd
from collections import defaultdict
from itertools import repeat

def parse(A):
    return np.array(A.strip().split(), 'c').T


def _range(start, stop, step):
    """
    Like range except it just iters start forever if step = 0
    """
    if step == 0:
        yield from repeat(start)
    else:
        yield from range(start, stop, step)

def find_reachable(A):
    reachable = defaultdict(list)

    for i in np.ndindex(*A.shape):
        if A[i] == b'.':
            continue
        for j in np.ndindex(*A.shape):
            if j == i:
                continue
            if A[j] == b'.':
                continue
            g = gcd(j[1] - i[1], j[0] - i[0])
            num = (j[1] - i[1])//g
            den = (j[0] - i[0])//g
            points = zip(_range(i[0], j[0], den), _range(i[1], j[1], num))
            next(points) # First point is one of i or j
            for x, y in points:
                if A[x, y] != b'.':
                    break
            else:
                reachable[i].append(j)
    return reachable

def print_reachable(reachable, shape):
    A = np.zeros(shape, dtype=np.int64)
    for i in reachable:
        A[i] = len(reachable[i])

    for row in A.T:
        for col in row:
            if col == 0:
                print('.', end='')
            else:
                print(col, end='')
        print()

def best(reachable):
    return max(reachable, key=lambda x: len(reachable[x]))

def get_angle(X):
    def angle(i):
        x, y = i[0] - X[0], i[1] - X[1]
        if x == 0:
            return 0 # instead of 2*pi
        return np.arctan2(-x, y) + np.pi
    return angle

def lasored_order(A, X):
    A = A.copy()
    angle = get_angle(X)
    while True:
        reachable = find_reachable(A)
        if not reachable:
            break
        for coord in sorted(reachable[X], key=angle):
            A[coord] = b'.'
            yield coord

ans = []
test_inputs = []

ans.append("Should get (3, 4) with 8")
test_inputs.append("""
.#..#
.....
#####
....#
...##
""")

ans.append("Should get (5, 8) with 33")
test_inputs.append("""
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
""")

ans.append("Should get (1, 2) with 35")
test_inputs.append("""
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
""")

ans.append("Should get (6, 3) with 41")
test_inputs.append("""
.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
""")

ans.append("Should get (11, 13) with 210")
test_inputs.append("""
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
""")

angle_test = """
.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##
"""

ans.append("Day 10 part 1")
input = """
#..#.#.#.######..#.#...##
##.#..#.#..##.#..######.#
.#.##.#..##..#.#.####.#..
.#..##.#.#..#.#...#...#.#
#...###.##.##..##...#..#.
##..#.#.#.###...#.##..#.#
###.###.#.##.##....#####.
.#####.#.#...#..#####..#.
.#.##...#.#...#####.##...
######.#..##.#..#.#.#....
###.##.#######....##.#..#
.####.##..#.##.#.#.##...#
##...##.######..##..#.###
...###...#..#...#.###..#.
.#####...##..#..#####.###
.#####..#.#######.###.##.
#...###.####.##.##.#.##.#
.#.#.#.#.#.##.#..#.#..###
##.#.####.###....###..##.
#..##.#....#..#..#.#..#.#
##..#..#...#..##..####..#
....#.....##..#.##.#...##
.##..#.#..##..##.#..##..#
.##..#####....#####.#.#.#
#..#..#..##...#..#.#.#.##
"""

if __name__ == '__main__':
    for a, I in zip(ans, test_inputs + [input]):
        print(a)
        A = parse(I)
        reachable = find_reachable(A)
        print_reachable(reachable, A.shape)
        b = best(reachable)
        print("Max", b, "with", len(reachable[b]), "reachable")
        print()

    A = parse(angle_test)
    reachable = find_reachable(A)
    X = np.where(A == b'X')
    X = X[0][0], X[1][0]
    print("Order for angle test input")
    print(sorted(reachable[X], key=get_angle(X)))
    print()

    large_input = test_inputs[-1]
    A = parse(large_input)
    reachable = find_reachable(A)
    X = best(reachable)
    print("Test Lasor")
    for i, coord in enumerate(lasored_order(A, X), 1):
        print("%s: %s" % (i, coord), end=' ')
        if i == 200:
            i200 = coord
    print()
    print("200th was", i200)
    print()

    A = parse(input)
    reachable = find_reachable(A)
    X = best(reachable)
    print("Day 10 part 1 Lasor")
    for i, coord in enumerate(lasored_order(A, X), 1):
        print("%s: %s" % (i, coord), end=' ')
        if i == 200:
            i200 = coord
    print()
    print("200th was", i200)
    print(100*i200[0] + i200[1])
