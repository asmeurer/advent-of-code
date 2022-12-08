test_input = """
30373
25512
65332
33549
35390
"""

input = open('day08_input').read()

import numpy as np

def parse_input(data):
    return np.array([[int(i) for i in line] for line in
                     data.strip().splitlines()])


def get_visible(trees):
    rows, cols = trees.shape
    visible = np.full_like(trees, 0)
    for row in range(rows):
        height = -1
        for i in range(cols):
            visible[row, i] |= trees[row, i] > height
            height = max(height, trees[row, i])

        height = -1
        for i in reversed(range(cols)):
            visible[row, i] |= trees[row, i] > height
            height = max(height, trees[row, i])

    for col in range(cols):
        height = -1
        for i in range(rows):
            visible[i, col] |= trees[i, col] > height
            height = max(height, trees[i, col])

        height = -1
        for i in reversed(range(rows)):
            visible[i, col] |= trees[i, col] > height
            height = max(height, trees[i, col])

    return visible

def part1(trees):
    return np.count_nonzero(get_visible(trees))

print("Day 8")
print("Part 1")
print("Test input")
test_trees = parse_input(test_input)
trees = parse_input(input)
print(test_trees)
print(get_visible(test_trees))
print(part1(test_trees))
print("Puzzle input")
print(part1(trees))
