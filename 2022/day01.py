test_input = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

import heapq

input = open('day01_input').read()

def parse(data):
    elves = data.strip().split('\n\n')
    elves = [[int(i) for i in e.splitlines()] for e in elves]
    return elves

def part1(data):
    elves = parse(data)
    m = max(elves, key=sum)
    return sum(m)

def part2(data):
    elves = parse(data)
    largest = heapq.nlargest(3, elves, key=sum)
    return sum(map(sum, largest))

print("Day 1")
print("Part 1")
print("Test input")
print(part1(test_input))
print("Puzzle input")
print(part1(input))
print("Part 2")
print("Test input")
print(part2(test_input))
print("Puzzle input")
print(part2(input))
