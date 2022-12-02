test_input = """
A Y
B X
C Z
"""

input = open('day02_input').read()

import numpy as np

# 0: rock
# 1: paper
# 2: scissors

def parse_input(text):
    lines = text.strip().splitlines()
    games = np.empty((len(lines), 2), dtype=int)

    mapping = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
    for i in range(len(lines)):
        elf, you = lines[i].split()
        games[i] = [mapping[elf], mapping[you]]
    return games

def score(elf, you):
    shape_score = you + 1
    if (elf, you) in [(0, 2), (1, 0), (2, 1)]:
        # loss
        game_score = 0
    elif elf == you:
        # draw
        game_score = 3
    else:
        # win
        game_score = 6
    return shape_score + game_score

def part1(games):
    return sum(score(elf, you) for elf, you in games)

print("Day 2")
print("Part 1")
print("Test input")
test_games = parse_input(test_input)
print(test_games)
print(part1(test_games))
print("Puzzle input")
games = parse_input(input)
print(part1(games))
