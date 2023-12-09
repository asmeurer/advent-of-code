test_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip()

puzzle_input = open("day09_input").read().strip()

import numpy as np

from sympy import symbols, interpolate

x = symbols('x')
def parse_input(input):
    sequences = []
    for line in input.splitlines():
        sequences.append(np.array([int(i) for i in line.split()]))
    return sequences

def get_poly(sequence):
    for d in range(1, len(sequence)):
        if np.all(np.diff(sequence, d) == 0):
            break
    return interpolate(sequence[:d], x)

def part1(sequences):
    vals = []
    for sequence in sequences:
        poly = get_poly(sequence)
        val = poly.subs(x, len(sequence)+1)
        vals.append(val)
    return sum(vals)

def part2(sequences):
    vals = []
    for sequence in sequences:
        poly = get_poly(sequence)
        val = poly.subs(x, 0)
        vals.append(val)
    return sum(vals)

if __name__ == "__main__":
    print("Day 9")
    print("Part 1")
    print("Test input")
    test_sequences = parse_input(test_input)
    print(part1(test_sequences))
    print("Puzzle input")
    puzzle_sequences = parse_input(puzzle_input)
    print(part1(puzzle_sequences))
    print("Part 2")
    print("Test input")
    print(part2(test_sequences))
    print("Puzzle input")
    print(part2(puzzle_sequences))
