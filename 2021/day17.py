test_input = "target area: x=20..30, y=-10..-5"

input = "target area: x=139..187, y=-148..-89"

import re

INPUT = re.compile(r"target area: x=([\d-]+)\.\.([\d-]+), y=([\d-]+)\.\.([\d-]+)")

import numpy as np
import numba

def parse_input(text):
    x1, x2, y1, y2 = map(int, INPUT.match(text).groups())
    return (x1, x2), (y1, y2)

@numba.njit
def step(pos, vel):
    pos = pos + vel
    delta = np.array([-1 if vel[0] > 0 else 0 if vel[0] == 0 else 1, -1])
    vel = vel + delta
    return pos, vel

@numba.njit
def run(box, vel):
    pos = np.array([0, 0])
    maxy = 0
    (x1, x2), (y1, y2) = box
    corner1 = np.array([x1, y1])
    corner2 = np.array([x2, y2])
    while True:
        if np.all((corner1 <= pos) & (pos <= corner2)):
            return maxy
        if pos[1] < y2:
            return False
        pos, vel = step(pos, vel)
        maxy = max(pos[1], maxy)

@numba.njit
def part1(box):
    unchanged = 0
    maxy = 0
    for y in range(1000):
        m = maxy
        print(y, maxy)
        for x in range(-1000, 1000):
            maxy = max(maxy, run(box, np.array([x, y])))
        if m != maxy:
            m = maxy
            unchanged = 0
        else:
            unchanged += 1
            if unchanged > 20:
                break
    return maxy

print("Day 17")
print("Part 1")
print("Test input")
test_data = parse_input(test_input)
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
data = parse_input(input)
ans = part1(data)
print(ans)
