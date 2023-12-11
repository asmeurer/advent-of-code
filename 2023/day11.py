test_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip()

puzzle_input = open('day11_input').read().strip()

import numpy as np

def parse_input(input):
    return np.array([[i == '#' for i in line] for line in input.splitlines()])

def empty_rows(puzzle):
    return np.argwhere(np.all(~puzzle, axis=1)).flatten()

def empty_cols(puzzle):
    return np.argwhere(np.all(~puzzle, axis=0)).flatten()

def distance(puzzle, a, b, multiple=2):
    rows = empty_rows(puzzle)
    cols = empty_cols(puzzle)
    xvals = np.searchsorted(rows, [a[0], b[0]])
    yvals = np.searchsorted(cols, [a[1], b[1]])
    return (abs(b[1] - a[1]) + abs(b[0] - a[0]) +
            abs(xvals[1] - xvals[0])*(multiple-1) + abs(yvals[1] - yvals[0])*(multiple-1))

def part1_2(puzzle, multiple=1):
    distances = []
    galaxies = np.argwhere(puzzle)
    for i in range(galaxies.shape[0]):
        for j in range(i + 1, galaxies.shape[0]):
            distances.append(distance(puzzle, galaxies[i], galaxies[j], multiple=multiple))

    return sum(distances)

if __name__ == '__main__':
    print("Day 11")
    print("Part 1")
    print("Test input")
    test_puzzle = parse_input(test_input)
    print(part1_2(test_puzzle))
    print("Puzzle input")
    puzzle = parse_input(puzzle_input)
    print(part1_2(puzzle))

    print("Part 2")
    print("Test input")
    print(part1_2(test_puzzle, multiple=10))
    print(part1_2(test_puzzle, multiple=100))

    print("Puzzle input")
    print(part1_2(puzzle, multiple=1_000_000))
