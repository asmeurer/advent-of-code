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
    if (x, y) == (a, b):
        new_tail = tail
    elif x == a and (y == b + 1 or y == b - 1):
        new_tail = tail
    elif y == b and (x == a + 1 or x == a - 1):
        new_tail = tail
    elif x == a:
        new_tail = x, y - sign(y - b)
    elif y == b:
        new_tail = x - sign(x - a), y
    else:
        new_tail = x - sign(x - a), y - sign(y - b)

print("Day 9")
print("Part 1")
print("Test input")
