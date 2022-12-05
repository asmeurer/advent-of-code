test_input = """\
    [D]    \n\
[N] [C]    \n\
[Z] [M] [P]\n\
 1   2   3 \n\

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

input = open('day05_input').read()

import re
from copy import deepcopy

def parse_input(data):
    INSTRUCTION = re.compile(r'move (\d+) from (\d+) to (\d+)')
    crates_s, instructions_s = data.split('\n\n')
    instructions = []
    for line in instructions_s.strip().splitlines():
        m = INSTRUCTION.match(line)
        instructions.append(list(map(int, m.groups())))

    # ncrates is a single digit number
    ncrates = int(crates_s.strip()[-1])
    crates = [[] for i in range(ncrates)]
    CRATE = re.compile(r'(\[[A-Z]\]|   ) ?'*ncrates)
    for line in crates_s.splitlines()[::-1]:
        if '1' in line:
            continue
        m = CRATE.match(line)
        if m is None:
            raise ValueError(f"Crate didn't match: {line!r}, {CRATE!r}")
        for c, i in zip(crates, m.groups()):
            if i.startswith('['):
                c.append(i[1])

    return crates, instructions

def move(crates, instruction):
    n, i1, i2 = instruction
    c1, c2 = crates[i1-1], crates[i2-1]

    c1[:], rest = c1[:-n], c1[-n:][::-1]
    c2.extend(rest)

def move_all(crates, instructions, _debug=False):
    crates = deepcopy(crates)
    if _debug: print(crates)
    for instruction in instructions:
        move(crates, instruction)
        if _debug: print(crates)
    return crates

def part1(crates, instructions, _debug=False):
    crates = move_all(crates, instructions, _debug=_debug)
    return ''.join([i[-1] for i in crates])

print("Day 5")
print("Part 1")
test_crates, test_instructions = parse_input(test_input)
print(test_crates)
print(test_instructions)
crates, instructions = parse_input(input)
print("Test input")
test_res = part1(test_crates, test_instructions, _debug=True)
print(test_res)
res = part1(crates, instructions)
print(res)
