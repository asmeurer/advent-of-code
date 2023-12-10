test_input1 = """
.....
.S-7.
.|.|.
.L-J.
.....
""".strip()

test_input2 = """
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
""".strip()

test_input3 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".strip()

test_input4 = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
""".strip()

puzzle_input = open('day10_input').read().strip()

import numpy as np

def parse_input(input):
    return np.array([list(line) for line in input.splitlines()])

dirs = {
    '|': "NS",
    '-': "EW",
    'L': "NE",
    'J': "NW",
    '7': "SW",
    'F': "SE",
}

directions = {
    "N": np.array([-1, 0]),
    "S": np.array([1, 0]),
    "E": np.array([0, 1]),
    "W": np.array([0, -1]),
}

opp_directions = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E",
}

def find_start(puzzle):
    return np.argwhere(puzzle == 'S')[0]

def other_element(x, L):
    assert x in L, f"{x} not in {L}"
    return L[1] if x == L[0] else L[0]

def walk(puzzle, position, direction):
    curr_tile = puzzle[tuple(position)]
    new_direction = other_element(opp_directions[direction], dirs[curr_tile])
    new_position = position + directions[new_direction]
    return new_position, new_direction

def get_start_direction(puzzle, start):
    for direction in "NSEW":
        tile = puzzle[tuple(start + directions[direction])]
        if tile == '.':
            continue
        if opp_directions[direction] in dirs[tile]:
            return direction
    raise RuntimeError("No start direction found")

def part1(puzzle):
    start = find_start(puzzle)
    direction = get_start_direction(puzzle, start)
    position = start + directions[direction]
    for i in range(1, puzzle.size):
        position, direction = walk(puzzle, position, direction)
        if np.all(position == start):
            return (i + 1)//2
    raise RuntimeError("No loop found")

if __name__ == '__main__':
    print("Day 10")
    print("Part 1")
    print("Test input 1")
    test_puzzle1 = parse_input(test_input1)
    print(part1(test_puzzle1))
    print("Test input 2")
    test_puzzle2 = parse_input(test_input2)
    print(part1(test_puzzle2))
    print("Test input 3")
    test_puzzle3 = parse_input(test_input3)
    print(part1(test_puzzle3))
    print("Test input 4")
    test_puzzle4 = parse_input(test_input4)
    print(part1(test_puzzle4))
    print("Puzzle input")
    puzzle = parse_input(puzzle_input)
    print(part1(puzzle))
