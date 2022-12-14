test_input = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

input = open('day14_input').read()

import sys
import subprocess
from collections import defaultdict

def closed_interval(x, y):
    x, y = sorted([x, y])
    yield from range(x, y + 1)

# 0 = air
# 1 = rock
# 2 = sand

def parse_input(data):
    rocks = defaultdict(int)

    for line in data.strip().splitlines():
        prev = None
        for coord in line.split(' -> '):
            x, y = map(int, coord.split(','))
            if prev is None:
                prev = x, y
                continue
            x0, y0 = prev
            if x == x0:
                for i in closed_interval(y0, y):
                    rocks[x, i] = 1
            elif y == y0:
                for i in closed_interval(x0, x):
                    rocks[i, y] = 1
            else:
                raise ValueError(f"Not a vertical or horizontal line: {x0, y0} -> {x, y}")
            prev = x, y

    return rocks

def print_rocks(rocks, clear=True):
    xs = [x for x, y in rocks]
    ys = [y for x, y in rocks]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)

    # print('min/max x', minx, maxx)
    # print('min/max y', miny, maxy)
    lines = []
    for y in range(miny, maxy+1):
        line = f"{y:>3} "
        for x in range(minx, maxx+1):
            if (x, y) not in rocks or rocks[x, y] == 0:
                line += '. '
            elif rocks[x, y] == 1:
                line += '# '
            elif rocks[x, y] == 2:
                line += 'o '
            else:
                raise ValueError(f"Unexpected value: {x, y, rocks[x, y]}")
        lines.append(line)

    l = len(lines[0])
    lines.insert(0, "   {minx:<l}{maxx:>l}".replace('l', str((l - 2)//2)).format(minx=minx, maxx=maxx))
    print('\n'.join(lines))
    if clear:
        sys.stdout.flush()
        subprocess.run('clear')

def fall(rocks, sand):
    x, y = sand
    assert rocks[x, y] == 2
    for coord in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
        if rocks[coord] == 0:
            rocks[sand] = 0
            rocks[coord] = 2
            return coord
    return sand

sand1 = (500, 0)

def fall_till_rest(rocks):
    maxy = max([y for x, y in rocks])

    sand = sand1
    rocks[sand] = 2
    while sand != (sand := fall(rocks, sand)):
        if sand[1] > maxy:
            return False
        # print_rocks(rocks)
    print_rocks(rocks)
    return True

def part1(rocks):
    i = 0
    while fall_till_rest(rocks):
        i += 1
    return i

def fall2(rocks, sand, maxy):
    x, y = sand
    assert rocks[x, y] == 2
    for coord in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
        if coord[1] >= maxy:
            rocks[coord[0], maxy+2] = 1
        if rocks[coord] == 0:
            rocks[sand] = 0
            rocks[coord] = 2
            return coord
    return sand

def fall_till_rest2(rocks, maxy):
    sand = sand1
    rocks[sand] = 2
    while sand != (sand := fall2(rocks, sand, maxy)):
        pass
        # print_rocks(rocks)
    if sand == sand1:
        return False
    # print_rocks(rocks)
    return True

def part2(rocks):
    maxy = max([y for x, y in rocks])

    i = 1
    while fall_till_rest2(rocks, maxy):
        i += 1
        if i % 20 == 0:
            print_rocks(rocks, clear=False)
    return i

print("Day 14")
print("Part 1")
print("Test input")
test_rocks = parse_input(test_input)
# print_rocks(test_rocks)
# print(part1(test_rocks), "steps")
print("Puzzle input")
rocks = parse_input(input)
# print_rocks(rocks)
# print(part1(rocks), "steps")
print("Part 2")
print("Test input")
test_rocks = parse_input(test_input)
print(part2(test_rocks), "steps")
print("Puzzle input")
rocks = parse_input(input)
print(part2(rocks), "steps")
