test_input = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

input = open('day03_input').read()

def parse_input(data):
    return data.strip().splitlines()

def part1(rucksacks):
    common = []
    for items in rucksacks:
        l = len(items)
        part1, part2 = items[:l//2], items[l//2:]
        sack_common = set(part1).intersection(set(part2))
        common.extend(list(sack_common))

    return sum(prio(i) for i in common)

def prio(x):
    if x.islower():
        return ord(x) - (ord('a') - 1)
    elif x.isupper():
        return ord(x) - (ord('A') - 27)

print("Day 3")
print("Part 1")
print("Test input")
test_rucksacks = parse_input(test_input)
rucksacks = parse_input(input)
print(part1(test_rucksacks))
print(part1(rucksacks))
