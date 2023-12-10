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

test_input5 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""".strip()

test_input6 = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""".strip()

test_input7 = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
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
            yield direction

def start_tile_type(puzzle, start):
    start_directions = set(get_start_direction(puzzle, start))
    for d in dirs:
        if set(dirs[d]) == start_directions:
            return d
    raise RuntimeError("No start tile type found")

def part1(puzzle):
    start = find_start(puzzle)
    direction = next(get_start_direction(puzzle, start))
    position = start + directions[direction]
    for i in range(1, puzzle.size):
        position, direction = walk(puzzle, position, direction)
        if np.all(position == start):
            return (i + 1)//2
    raise RuntimeError("No loop found")

def part2(puzzle, verbose=False):
    # First create a mask of the edge points of the loop
    loop = np.zeros_like(puzzle, dtype=bool)
    start = find_start(puzzle)
    loop[tuple(start)] = True
    direction = next(get_start_direction(puzzle, start))
    position = start + directions[direction]
    loop[tuple(position)] = True
    for i in range(1, puzzle.size):
        position, direction = walk(puzzle, position, direction)
        loop[tuple(position)] = True
        if np.all(position == start):
            break

    puzzle = np.where(loop, puzzle, '.')
    puzzle[tuple(start)] = start_tile_type(puzzle, start)
    # Ray casting: Cast a ray from a point to the left edge and count how many
    # edges there are. Since the points align with the horizontal edges, we
    # imagine they are shifted up slightly, so that they only intersect with
    # |, J, and L.
    edges = np.array(['|', 'J', 'L'])
    ray_cast = np.cumsum(np.isin(puzzle, edges), axis=1)
    interior = (ray_cast % 2 == 1) & ~loop
    if verbose:
        for i, j in np.ndindex(puzzle.shape):
            if loop[i, j]:
                print(puzzle[i, j], end='')
            elif interior[i, j]:
                print('I', end='')
            else:
                print('O', end='')
            if j == puzzle.shape[1] - 1:
                print()
        print()
    return np.sum(interior)

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
    print("Part 2")
    print("Test input 1")
    print(part2(test_puzzle1, verbose=True))
    print("Test input 2")
    print(part2(test_puzzle2, verbose=True))
    print("Test input 3")
    print(part2(test_puzzle3, verbose=True))
    print("Test input 4")
    print(part2(test_puzzle4, verbose=True))
    print("Test input 5")
    test_puzzle5 = parse_input(test_input5)
    print(part2(test_puzzle5, verbose=True))
    print("Test input 6")
    test_puzzle6 = parse_input(test_input6)
    print(part2(test_puzzle6, verbose=True))
    print("Test input 7")
    test_puzzle7 = parse_input(test_input7)
    print(part2(test_puzzle7, verbose=True))
    print("Puzzle input")
    print(part2(puzzle, verbose=True))
