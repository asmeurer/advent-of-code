test_input = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

input = open('day04_input').read()

def parse_input(data):
    res = []
    for line in data.strip().splitlines():
        p1, p2 = line.split(',')
        p1a, p1b = map(int, p1.split('-'))
        p2a, p2b = map(int, p2.split('-'))
        res.append([(p1a, p1b), (p2a, p2b)])
    return res

def part1(pairs):
    return sum(
           p1a >= p2a and p1b <= p2b
        or p2a >= p1a and p2b <= p1b
    for (p1a, p1b), (p2a, p2b) in pairs)

print("Day 4")
print("Part 1")
print("Test input")
test_pairs = parse_input(test_input)
pairs = parse_input(input)
print(test_pairs)
print(part1(test_pairs))
print(part1(pairs))
