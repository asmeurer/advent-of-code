test_input = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

input = open('day13_input').read()

from functools import total_ordering

def parse_input(data):
    packets = []
    for lines in data.strip().split('\n\n'):
        packets.append(tuple([IntList(eval(i)) for i in lines.splitlines()]))
    return packets

@total_ordering
class IntList:
    def __init__(self, l):
        if isinstance(l, list):
            l = [IntList(i) for i in l]
        self.l = l
        self.norml = self.l if isinstance(self.l, list) else [self.l]


    def __lt__(self, other):
        if isinstance(other, IntList):
            return self.norml < other.norml
        elif isinstance(other, (int, list)):
            return self < IntList(other)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, IntList):
            return self.norml == other.norml
        return self.l == other or self.norml == other

    def __repr__(self):
        return repr(self.l)

def part1(packets):
    right_order = [i < j for i, j in packets]
    print(right_order)
    return sum(i + 1 for i in range(len(right_order)) if right_order[i])

dividers = [IntList([[2]]), IntList([[6]])]

def part2(packets):
    all_packets = [i for i, j in packets] + [j for i, j in packets] + dividers
    sorted_packets = sorted(all_packets)
    print(sorted_packets)
    indices = sorted_packets.index(dividers[0]) + 1, sorted_packets.index(dividers[1]) + 1
    print(indices)
    return indices[0]*indices[1]

print("Day 13")
print("Part 1")
print("Test input")
test_packets = parse_input(test_input)
print(test_packets)
print(part1(test_packets))
print("Puzzle input")
packets = parse_input(input)
print(part1(packets))
print("Part 2")
print("Test input")
print(part2(test_packets))
print("Puzzle input")
print(part2(packets))
