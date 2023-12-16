test_input = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
""".strip()

# Note:
#
#   dx
# +---->
# |
# | dy
# |
# v
#
# And note grid is (y, x)

puzzle_input = open('day16_input').read().strip()

import sys
sys.setrecursionlimit(10000)

import numpy as np

def parse_input(input):
    return np.array([list(line) for line in input.splitlines()])


energized_types = {
    (0, 1): 1,
    (1, 0): 1<<1,
    (0, -1): 1<<2,
    (-1, 0): 1<<3,
}

def shine_beam(grid, energized, x, y, dx, dy):
    new_x, new_y = x + dx, y + dy
    if (new_x < 0 or new_x >= grid.shape[1] or
        new_y < 0 or new_y >= grid.shape[0]):
        return

    if energized[new_y, new_x] & energized_types[(dx, dy)]:
        return

    # print_energized(energized)
    # print()

    energized[new_y, new_x] |= energized_types[(dx, dy)]

    match grid[new_y, new_x]:
        case '.':
            shine_beam(grid, energized, new_x, new_y, dx, dy)
        case '|':
            shine_beam(grid, energized, new_x, new_y, 0, -1)
            shine_beam(grid, energized, new_x, new_y, 0, +1)
        case '-':
            shine_beam(grid, energized, new_x, new_y, -1, 0)
            shine_beam(grid, energized, new_x, new_y, +1, 0)
        case '/':
            match (dx, dy):
                case (1, 0):
                    shine_beam(grid, energized, new_x, new_y, 0, -1)
                case (0, 1):
                    shine_beam(grid, energized, new_x, new_y, -1, 0)
                case (-1, 0):
                    shine_beam(grid, energized, new_x, new_y, 0, 1)
                case (0, -1):
                    shine_beam(grid, energized, new_x, new_y, 1, 0)
        case '\\':
            match (dx, dy):
                case (1, 0):
                    shine_beam(grid, energized, new_x, new_y, 0, 1)
                case (0, 1):
                    shine_beam(grid, energized, new_x, new_y, 1, 0)
                case (-1, 0):
                    shine_beam(grid, energized, new_x, new_y, 0, -1)
                case (0, -1):
                    shine_beam(grid, energized, new_x, new_y, -1, 0)

def print_energized(energized):
    for y in range(energized.shape[0]):
        for x in range(energized.shape[1]):
            if energized[y, x]:
                print('#', end='')
            else:
                print('.', end='')
        print()

def part1(grid, verbose=True):
    x, y = -1, 0
    dx, dy = 1, 0
    energized = np.zeros_like(grid, dtype=int)
    shine_beam(grid, energized, x, y, dx, dy)
    if verbose:
        print_energized(energized)
    return np.sum(energized != 0)

if __name__ == '__main__':
    print("Day 16")
    print("Part 1")
    print("Test input")
    test_grid = parse_input(test_input)
    print(test_input)
    print()
    print(part1(test_grid))
    print("Puzzle input")
    puzzle_grid = parse_input(puzzle_input)
    print(part1(puzzle_grid, verbose=False))
