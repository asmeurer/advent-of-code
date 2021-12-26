test_input = "target area: x=20..30, y=-10..-5"
test_input2 = """
23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
8,-2    27,-8   30,-5   24,-7
"""

input = "target area: x=139..187, y=-148..-89"

import re

INPUT = re.compile(r"target area: x=([\d-]+)\.\.([\d-]+), y=([\d-]+)\.\.([\d-]+)")

import numpy as np
import numba
import matplotlib.pyplot as plt

def parse_input(text):
    x1, x2, y1, y2 = map(int, INPUT.match(text).groups())
    return (x1, x2), (y1, y2)

@numba.njit
def step(pos, vel):
    pos += vel
    delta = np.array([-1 if vel[0] > 0 else 0 if vel[0] == 0 else 1, -1])
    vel += delta

@numba.njit
def run(box, vel):
    pos = np.array([0, 0])
    maxy = 0
    (x1, x2), (y1, y2) = box
    corner1 = np.array([x1, y1])
    corner2 = np.array([x2, y2])
    while True:
        if np.all((corner1 <= pos) & (pos <= corner2)):
        # if x1 <= pos[0] <= x2 and y1 <= pos[1] <= y2:
            return maxy
        if pos[1] < y1:
            return -1
        step(pos, vel)
        maxy = max(pos[1], maxy)

@numba.njit
def part1(box):
    unchanged = 0
    maxy = 0
    for y in range(1000):
        m = maxy
        print(y, maxy)
        for x in range(1000):
            maxy = max(maxy, run(box, np.array([x, y])))
        if m != maxy:
            m = maxy
            unchanged = 0
        else:
            unchanged += 1
            if unchanged > 20:
                break
    return maxy

@numba.njit
def part2(box):
    unchanged = 0
    N = 0
    res = np.zeros((5000, 2), dtype=np.int64)
    for y in range(-1000, 1000):
        m = N
        if N > 0:
            print(y, N)
        for x in range(1000):
            if run(box, np.array([x, y])) >= 0:
                res[N] = (x, y)
                N += 1
        if m != N:
            m = N
            unchanged = 0
        else:
            unchanged += 1
            if N > 0 and unchanged > 50:
                break
    return res

test_data = parse_input(test_input)
data = parse_input(input)

if __name__ == '__main__':
    print("Day 17")
    print("Part 1")
    print("Test input")
    print(test_data)
    test_maxy72 = run(test_data, np.array([7, 2]))
    print(test_maxy72)
    test_maxy63 = run(test_data, np.array([6, 3]))
    print(test_maxy63)
    test_maxy90 = run(test_data, np.array([9, 0]))
    print(test_maxy90)
    test_maxy17_4 = run(test_data, np.array([17, -4]))
    print(test_maxy17_4)
    test_maxy69 = run(test_data, np.array([6, 9]))
    print(test_maxy69)

    test_ans = part1(test_data)
    print(test_ans)

    print("Puzzle input")

    ans = part1(data)
    print(ans)

    print("Part 2")
    print("Test input")

    test_ans2 = part2(test_data)
    N = np.nonzero(np.all(test_ans2 == np.array([0, 0]), axis=1))[0][0]
    # for i in range(N):
    #     print(test_ans2[i])
    correct_test_ans2 = set([tuple(map(int, i.split(','))) for i in
                             test_input2.strip().split()])
    test_ans2_set = set(map(tuple, test_ans2[:N]))
    print("In our answer but not in the correct answer:", test_ans2_set - correct_test_ans2)
    print("In the correct answer but not in our answer:", correct_test_ans2 - test_ans2_set)
    print(N)
    plt.scatter(test_ans2[:, 0], test_ans2[:, 1])
    plt.show()
    assert test_ans2_set == correct_test_ans2

    print("Puzzle input")
    ans2 = part2(data)
    print(np.nonzero(np.all(ans2 == np.array([0, 0]), axis=1))[0][0])
    plt.scatter(ans2[:, 0], ans2[:, 1])
    plt.show()
