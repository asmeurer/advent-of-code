test_input = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

input = open('day09_input').read()

def parse_input(data):
    instrs = []
    for line in data.strip().splitlines():
        dir, n = line.split()
        instrs.append((dir, int(n)))
    return instrs

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def move(head, tail, dir):
    a, b = head
    if dir == 'D':
        new_head = a-1, b
    elif dir == 'U':
        new_head = a+1, b
    elif dir == 'R':
        new_head = a, b+1
    elif dir == 'L':
        new_head = a, b-1
    else:
        raise ValueError(f"Unrecognized dir: {dir!r}")

    a, b = new_head
    x, y = tail
    if abs(x - a) in {-1, 0, 1} and abs(y - b) in {-1, 0, 1}:
        new_tail = tail
    else:
        new_tail = x - sign(x - a), y - sign(y - b)

    return new_head, new_tail

def part1(moves, _debug=False):
    head, tail = (0, 0), (0, 0)
    tail_positions = {tail}
    for dir, n in moves:
        for i in range(n):
            head, tail = move(head, tail, dir)
            tail_positions.add(tail)
            if _debug: print(head, tail)

    return len(tail_positions)


print("Day 9")
print("Part 1")
print("Test input")
test_moves = parse_input(test_input)
moves = parse_input(input)
print(part1(test_moves, _debug=True))
print("Puzzle input")
print(part1(moves))
