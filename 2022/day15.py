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

from sympy import Integers, Interval, Intersection, Range, Union, symbols, solve

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

def empty_in_row(points, row, maxn):
    interval = Union()
    for sensor, beacon in points:
        I = Interval(*min_max_x(sensor, beacon, row))
        interval |= I
    s = Intersection(Integers, interval, Interval(0, maxn))
    return set_size(s)

def circle(p, r, row):
    x, y = p
    if abs(y - row) > r:
        return
    yield (x + (r - abs(row - y)), row)
    yield (x - (r - abs(row - y)), row)

def get_positions(points, row):
    area = {}

    for sensor, beacon in points:
        area[beacon] = 1
        dist = manhattan(sensor, beacon)
        print(dist)
        for r in range(dist+1):
            for p in circle(sensor, r, row):
                # if manhattan(sensor, p) != r:
                #     breakpoint()
                area.setdefault(p, 0)

    return area

def find_beacon_old(points, maxn):
    for row in range(maxn):
        if row % 1000000 == 0:
            print(row)
        empty = empty_in_row(points, row, maxn)
        if empty != maxn + 1:
            break
    area = get_positions(points, row)
    cols = set(range(maxn+1)) - {x for x, y in area}
    assert len(cols) == 1, cols
    col = cols.pop()
    return col, row


def intersect_lines(p1, p2, d1, d2):
    """
    Yield the points where the 45 degree lines distance d1 from p1 and d2 from
    p2 intersect.

    Gives the nearest integer point if they don't intersect act an integer point.
    """
    x1, y1 = p1
    x2, y2 = p2

    d, x, y, x0, y0 = symbols('d x y x0 y0')
    lines = [
        d - x + x0 + y0,
        d + x - x0 + y0,
        d + x - x0 - y0,
        d - x + x0 - y0]

    for i in range(4):
        for j in range(4):
            l1 = lines[i].subs({d: d1, x0: x1, y0: y1})
            l2 = lines[j].subs({d: d2, x0: x2, y0: y2})
            sol = solve(l1 - l2, x)
            if not sol:
                continue
            xval = sol[0]
            yval = l1.subs(x, xval)

            yield (int(xval), int(yval))

def get_distances(points):
    return {sensor: manhattan(sensor, beacon) for sensor, beacon in points}

def nearby(p, k=2):
    x, y = p
    for i in range(-k, k+1):
        for j in range(-k, k+1):
            yield (x + i, y + j)

def check_distances(p, distances):
    for sensor, d in distances.items():
        if manhattan(p, sensor) <= d:
            return False
    return True

def find_beacon(points, maxn):
    distances = get_distances(points)
    n = len(points)
    for i in range(n):
        for j in range(i, n):
            p1, p2 = points[i][0], points[j][0]
            d1, d2 = distances[p1], distances[p2]
            for intersection in intersect_lines(p1, p2, d1, d2):
                # assert manhattan(intersection, p1) == d1, breakpoint()
                # assert manhattan(intersection, p2) == d2
                for p in nearby(intersection):
                    x, y = p
                    if not (0 <= x <= maxn) or not (0 <= y <= maxn):
                        continue
                    if check_distances(p, distances):
                        return p
    raise RuntimeError("Could not find point p")

def part2(points, maxn=4000000):
    col, row = find_beacon(points, maxn)
    print(col, row)
    return col*4000000 + row

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
print("Part 2")
print("Test input")
print(part2(test_points, maxn=20))
print("Puzzle input")
print(part2(points))
