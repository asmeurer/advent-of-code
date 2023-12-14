test_input = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip()

test_input2 = """
OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
""".strip()

puzzle_input = open('day14_input').read().strip()

import numpy as np

from numba import njit

vals = {
    '.': 0,
    '#' : 1,
    'O' : 2,
}

def parse_input(input):
    return np.array([[vals[c] for c in line] for line in input.splitlines()])

def print_grid(grid):
    for row in grid:
        print(''.join(['.#O'[c] for c in row]))
    print()

@njit
def tilt(grid):
    # grid = grid.copy()
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            c = grid[x, y]
            if c == 2:
                i = x - 1
                while i >= 0 and grid[i, y] == 0:
                    i -= 1
                grid[x, y] = 0
                grid[i+1, y] = 2
    return grid

@njit
def spin(grid):
    for i in range(4):
        grid = tilt(grid)[::-1].T
    return grid

@njit
def load(grid):
    return np.sum(np.arange(grid.shape[0], 0, -1)[:, None] * (grid == 2))

def part1(grid):
    tilted_grid = tilt(grid)
    # print_grid(tilted_grid)
    return load(tilted_grid)

@njit
def part2(grid, n):
    for i in range(n):
        if i % 1000000 == 0:
            print(i, '/', n, "(", i/n*100, "% )")
            # print(f"{i} / {n} ({i/n:.2%})")
        grid = spin(grid)
    return load(grid)

ncycles = 1000000000

if __name__ == '__main__':
    print("Day 14")
    print("Part 1")
    print("Test input")
    test_grid = parse_input(test_input)
    test_grid2 = parse_input(test_input2)
    print(part1(test_grid))
    print(part1(test_grid2))
    assert np.all(tilt(test_grid) == test_grid2)
    print("Puzzle input")
    puzzle_grid = parse_input(puzzle_input)
    print(part1(puzzle_grid))
    print("Part 2")
    print("Test input")
    print_grid(spin(test_grid))
    print_grid(spin(spin(test_grid)))
    print_grid(spin(spin(spin(test_grid))))
    # print(part2(test_grid, ncycles))
    print("Puzzle input")
    print(part2(puzzle_grid, ncycles))
