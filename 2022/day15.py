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

from sympy import Integers, Interval, Intersection, Range, Union

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

def min_max_x(sensor, beacon, row):
    x, y = sensor
    dist = manhattan(sensor, beacon)
    offset = (dist - abs(row - y))
    return x - offset, x + offset

def set_size(s):
    # len(Union(Range)) doesn't work
    if isinstance(s, Range):
        return len(s)
    elif isinstance(s, Union):
        return sum(len(i) for i in s.args)

def part1(points, row=2000000):
    beacons_in_row = set()

    interval = Union()
    for sensor, beacon in points:
        if beacon[1] == row:
            beacons_in_row.add(beacon)
        I = Interval(*min_max_x(sensor, beacon, row))
        interval |= I
    s = Intersection(Integers, interval)
    return set_size(s) - len(beacons_in_row)


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