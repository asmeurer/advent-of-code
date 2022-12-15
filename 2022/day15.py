test_input = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

input = open('day15_input').read()

import re

SENSOR_LINE = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

def parse_input(data):
    points = []
    for line in data.strip().splitlines():
        m = SENSOR_LINE.match(line)
        sx, sy, bx, by = map(int, m.groups())
        points.append([(sx, sy), (bx, by)])

    return points

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def circle(p, r):
    x, y = p
    # we need all points i, j s.t. |i| + |j| = r
    for i in range(-r, r+1):
        for j in range(-r, r+1):
            if abs(i) + abs(j) == r:
                yield (x + i, y + j)

def circle2(p, r, row):
    x, y = p
    if abs(y - row) > r:
        return
    yield (x + (r - row), row)
    yield (x - (r - row), row)

def get_positions(points, row):
    area = {}

    for sensor, beacon in points:
        area[beacon] = 1
        dist = manhattan(sensor, beacon)
        print(dist)
        for r in range(dist+1):
            for p in circle2(sensor, r, row):
                area.setdefault(p, 0)

    return area

def part1(points, row=2000000):
    area = get_positions(points, row)
    no_beacons = [(x, y) for (x, y) in area if y == row and area[x, y] == 0]
    return len(no_beacons)

print("Day 15")
print("Part 1")
print("Test input")
test_points = parse_input(test_input)
points = parse_input(input)
# print(test_points)
# test_area = get_positions(test_points)
# print(test_area)
print("Answer:", part1(test_points, row=10))
print("Puzzle input")
print("Answer:", part1(points))
