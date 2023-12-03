test_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()

puzzle_input = open("day03_input").read().strip()

from dataclasses import dataclass
from math import prod

@dataclass
class Number:
    value: int
    coords: list
    adjacent: list

@dataclass
class Symbol:
    value: str
    coord: tuple
    adjacent: list

def get_numbers_symbols(puzzle):
    numbers = []
    symbols = []

    for i, line in enumerate(puzzle.splitlines()):
        line += '.'
        num = ''
        for j, c in enumerate(line):
            if c.isdigit():
                num += c
            else:
                if num:
                    coords = [(i, k) for k in range(j-len(num), j)]
                    n = Number(int(num), coords, [])
                    numbers.append(n)
                    num = ''
                if c != '.':
                    s = Symbol(c, (i, j), [])
                    symbols.append(s)

    return numbers, symbols

def compute_adjacent(numbers, symbols):
    for s in symbols:
        x, y = s.coord
        for n in numbers:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (x + i, y + j) in n.coords:
                        n.adjacent.append(s)
                        s.adjacent.append(n)
                        break
def part1(puzzle):
    numbers, symbols = get_numbers_symbols(puzzle)
    compute_adjacent(numbers, symbols)

    return sum(n.value for n in numbers if n.adjacent)

def part2(puzzle):
    numbers, symbols = get_numbers_symbols(puzzle)
    compute_adjacent(numbers, symbols)
    gears = [s for s in symbols if s.value == '*' and len(s.adjacent) == 2]
    ratios = [prod(n.value for n in g.adjacent) for g in gears]
    return sum(ratios)

if __name__ == '__main__':
    print("Day 3")
    print("Part 1")
    print("Test input")
    print(part1(test_input))
    print("Puzzle input")
    print(part1(puzzle_input))
    print("Part 2")
    print("Test input")
    print(part2(test_input))
    print("Puzzle input")
    print(part2(puzzle_input))
