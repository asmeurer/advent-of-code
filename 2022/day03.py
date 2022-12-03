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

def prio(x):
    if x.islower():
        return ord(x) - (ord('a') - 1)
    elif x.isupper():
        return ord(x) - (ord('A') - 27)

def part1(rucksacks):
    common = []
    for items in rucksacks:
        l = len(items)
        part1, part2 = items[:l//2], items[l//2:]
        sack_common = set(part1).intersection(set(part2))
        common.extend(list(sack_common))

    return sum(prio(i) for i in common)

def part2(rucksacks):
    common = []
    for sack1, sack2, sack3 in zip(rucksacks[0::3], rucksacks[1::3], rucksacks[2::3]):
        badge = set(sack1).intersection(set(sack2)).intersection(set(sack3))
        assert len(badge) == 1
        common.append(badge.pop())
    return sum(prio(i) for i in common)

print("Day 3")
print("Part 1")
print("Test input")
test_rucksacks = parse_input(test_input)
rucksacks = parse_input(input)
print(part1(test_rucksacks))
print(part1(rucksacks))
print("Part 1")
print("Test input")
print(part2(test_rucksacks))
print(part2(rucksacks))
