test_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
puzzle_input = open('day15_input').read()

import numpy as np

def parse_input(input):
    assert '\n' not in input
    return input.split(',')

def hash(x):
    a = np.array([ord(c) for c in x] + [0], dtype=np.uint16)
    return np.polyval(a, 17) % 256

def part1(strings):
    return sum(hash(s) for s in strings)

if __name__ == '__main__':
    print("Day 15")
    print("Part 1")
    print("Test input")
    test_strings = parse_input(test_input)
    print(hash("HASH"))
    for s in test_strings:
        print(s, hash(s))
    print(part1(test_strings))
    print("Puzzle input")
    puzzle_strings = parse_input(puzzle_input)
    print(part1(puzzle_strings))
