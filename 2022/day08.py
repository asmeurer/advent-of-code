test_input = """
30373
25512
65332
33549
35390
"""

input = open('day08_input').read()

import numpy as np

from math import prod

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

def scenic_score(trees, i, j):
    rows, cols = trees.shape

    height = trees[i, j]
    scores = []

    score = 0
    for col in range(j-1, -1, -1):
        score += 1
        if trees[i, col] >= height:
            break
    scores.append(score)

    score = 0
    for row in range(i-1, -1, -1):
        score += 1
        if trees[row, j] >= height:
            break
    scores.append(score)

    score = 0
    for row in range(i+1, rows):
        score += 1
        if trees[row, j] >= height:
            break
    scores.append(score)

    score = 0
    for col in range(j+1, cols):
        score += 1
        if trees[i, col] >= height:
            break
    scores.append(score)

    return scores

def part1(trees):
    return np.count_nonzero(get_visible(trees))

def part2(trees):
    rows, cols = trees.shape
    scores = [scenic_score(trees, i, j) for i in range(rows) for j in range(cols)]
    return max([prod(score) for score in scores])

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
print("Part 2")
print("Test input")
print(scenic_score(test_trees, 1, 2))
print(scenic_score(test_trees, 3, 2))
print(part2(test_trees))
print("Puzzle input")
print(part2(trees))
