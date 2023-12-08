test_input1 = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip()

test_input2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip()

test_input3 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip()

puzzle_input = open('day08_input').read().strip()

from sympy import ilcm

def parse_input(input):
    _instructions, _nodes = input.split('\n\n')
    instructions = [int(i == 'R') for i in _instructions.strip()]
    nodes = {}
    for line in _nodes.strip().splitlines():
        name, children = line.split(' = ')
        children = children[1:-1].split(', ')
        nodes[name] = tuple(children)

    return instructions, nodes

def part1(instructions, nodes):
    curr = 'AAA'
    steps = 0
    while curr != 'ZZZ':
        for inst in instructions:
            steps += 1
            curr = nodes[curr][inst]
    return steps

def part2(instructions, nodes):
    start_nodes = [node for node in nodes if node.endswith('A')]
    end_nodes = [node for node in nodes if node.endswith('Z')]
    all_steps = []
    for start_node in start_nodes:
        curr = start_node
        steps = 0
        while curr not in end_nodes:
            for inst in instructions:
                steps += 1
                curr = nodes[curr][inst]
        all_steps.append(steps)
    return ilcm(*all_steps)

if __name__ == '__main__':
    print("Day 08")
    print("Part 1")
    print("Test input 1")
    test_instructions1, test_nodes1 = parse_input(test_input1)
    print(test_instructions1)
    print(test_nodes1)
    print(part1(test_instructions1, test_nodes1))
    print("Test input 2")
    test_instructions2, test_nodes2 = parse_input(test_input2)
    print(test_instructions2)
    print(test_nodes2)
    print(part1(test_instructions2, test_nodes2))
    print("Puzzle input")
    puzzle_instructions, puzzle_nodes = parse_input(puzzle_input)
    print(part1(puzzle_instructions, puzzle_nodes))
    print("Part 2")
    print("Test input 3")
    test_instructions3, test_nodes3 = parse_input(test_input3)
    print(part2(test_instructions3, test_nodes3))
    print("Puzzle input")
    print(part2(puzzle_instructions, puzzle_nodes))
