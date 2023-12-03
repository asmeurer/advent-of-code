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


def parse_input(puzzle):
    return puzzle.splitlines()

def get_numbers_symbols(puzzle):
    numbers = []
    symbols = []

    for i, line in enumerate(puzzle):
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

def part1(puzzle):
    numbers, symbols = get_numbers_symbols(puzzle)
    for s in symbols:
        x, y = s.coord
        for n in numbers:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (x + i, y + j) in n.coords:
                        n.adjacent.append(s)
                        s.adjacent.append(n)
                        break

    # for s in symbols:
    #     print(s.value, [n.value for n in s.adjacent])
    # for n in numbers:
    #     if not n.adjacent:
    #         print(n)
    #         if n.coords[0][1] == 0:
    #             print(puzzle[n.coords[0][0]-1][n.coords[0][1]:n.coords[-1][1]+2])
    #             print(puzzle[n.coords[0][0]][n.coords[0][1]:n.coords[-1][1]+2])
    #             print(puzzle[n.coords[0][0]+1][n.coords[0][1]:n.coords[-1][1]+2])
    #         else:
    #             if n.coords[0][0] != 0:
    #                 print(puzzle[n.coords[0][0]-1][n.coords[0][1]-1:n.coords[-1][1]+2])
    #             print(puzzle[n.coords[0][0]][n.coords[0][1]-1:n.coords[-1][1]+2])
    #             print(puzzle[n.coords[0][0]+1][n.coords[0][1]-1:n.coords[-1][1]+2])
    #         # print(n.value, [s.value for s in n.adjacent])

    # print(sum(n.value for n in numbers))
    # print(sum(set(n.value for n in numbers if n.adjacent)))
    return sum(n.value for n in numbers if n.adjacent)

if __name__ == '__main__':
    test_input = parse_input(test_input)
    puzzle_input = parse_input(puzzle_input)
    print("Day 3")
    print("Part 1")
    print("Test input")
    print(part1(test_input))
    print("Puzzle input")
    print(part1(puzzle_input))
