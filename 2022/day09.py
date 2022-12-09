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

test_input2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
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

def move2(new_head, tail):
    a, b = new_head
    x, y = tail
    if abs(x - a) in {-1, 0, 1} and abs(y - b) in {-1, 0, 1}:
        new_tail = tail
    else:
        new_tail = x - sign(x - a), y - sign(y - b)

    return new_tail

def part2(moves, _debug=False):
    head, *TAILS = [(0, 0)]*10
    tail9_positions = {TAILS[-1]}
    for dir, n in moves:
        for i in range(n):
            head, t0 = move(head, TAILS[0], dir)
            NEW_TAILS = [t0]
            for t in TAILS[1:]:
                t = move2(NEW_TAILS[-1], t)
                NEW_TAILS.append(t)

            TAILS = NEW_TAILS
            tail9_positions.add(TAILS[-1])
            if _debug: print(head, *TAILS)
    return len(tail9_positions)

print("Day 9")
print("Part 1")
print("Test input")
test_moves = parse_input(test_input)
moves = parse_input(input)
print(part1(test_moves, _debug=True))
print("Puzzle input")
print(part1(moves))
print("Part 1")
print("Test input1")
print(part2(test_moves, _debug=True))
print("Test input 2")
test_moves2 = parse_input(test_input2)
print(part2(test_moves2, _debug=True))
print("Puzzle input")
print(part2(moves))
