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

def score1(elf, you):
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

# 0: lose
# 1: draw
# 2: win

def score2(elf, you):
    game_score = you*3
    if (elf, you) in [(0, 1), (1, 0), (2, 2)]:
        # rock
        shape_score = 1
    elif (elf, you) in [(0, 2), (1, 1), (2, 0)]:
        # paper
        shape_score = 2
    else:
        # scissors
        shape_score = 3
    return shape_score + game_score

def part1(games):
    return sum(score1(elf, you) for elf, you in games)

def part2(games):
    return sum(score2(elf, you) for elf, you in games)

print("Day 2")
print("Part 1")
print("Test input")
test_games = parse_input(test_input)
print(test_games)
print(part1(test_games))
print("Puzzle input")
games = parse_input(input)
print(part1(games))
print("Part 2")
print("Test input")
test_games = parse_input(test_input)
print(test_games)
print(part2(test_games))
print("Puzzle input")
games = parse_input(input)
print(part2(games))
