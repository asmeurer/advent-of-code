test_input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip()

puzzle_input = open('day13_input').read().strip()

import numpy as np

def parse_input(text):
    blocks = []
    for block in text.split('\n\n'):
        blocks.append(np.array([[c == '#' for c in line] for line in
                                block.splitlines()], dtype=int))
    return blocks

def part1(blocks):
    rows = []
    cols = []
    for block in blocks:
        x, y = block.shape
        for i in range(1, x):
            a = block[i:i+min(i, x-i)][::-1]
            b = block[i-min(i, x-i):i]
            if np.all(a == b):
                rows.append(i)
                break
        for j in range(1, y):
            a = block[:, j:j+min(j, y-j)][:, ::-1]
            b = block[:, j-min(j, y-j):j]
            if np.all(a == b):
                cols.append(j)
                break
    return 100*sum(rows) + sum(cols)


def part2(blocks):
    rows = []
    cols = []
    for block in blocks:
        # Find the initial reflection line
        x, y = block.shape
        r = c = -1
        for i in range(1, x):
            a = block[i:i+min(i, x-i)][::-1]
            b = block[i-min(i, x-i):i]
            if np.all(a == b):
                r = i
                break
        for j in range(1, y):
            a = block[:, j:j+min(j, y-j)][:, ::-1]
            b = block[:, j-min(j, y-j):j]
            if np.all(a == b):
                c = j
                break

        found = False
        for idx in np.ndindex(block.shape):
            bl = block.copy()
            bl[idx] ^= 1
            for i in range(1, x):
                if i == r:
                    continue
                a = bl[i:i+min(i, x-i)][::-1]
                b = bl[i-min(i, x-i):i]
                if np.all(a == b):
                    rows.append(i)
                    found = True
                    break
            for j in range(1, y):
                if j == c:
                    continue
                a = bl[:, j:j+min(j, y-j)][:, ::-1]
                b = bl[:, j-min(j, y-j):j]
                if np.all(a == b):
                    cols.append(j)
                    found = True
                    break
            if found:
                # print(f"smudge at {idx}")
                # print(rows, cols)
                break
    return 100*sum(rows) + sum(cols)

if __name__ == '__main__':
    print("Day 13")
    print("Part 1")
    print("Test input")
    test_blocks = parse_input(test_input)
    print(part1(test_blocks))
    print("Puzzle input")
    puzzle_blocks = parse_input(puzzle_input)
    print(part1(puzzle_blocks))
    print("Part 2")
    print("Test input")
    print(part2(test_blocks))
    print("Puzzle input")
    print(part2(puzzle_blocks))
