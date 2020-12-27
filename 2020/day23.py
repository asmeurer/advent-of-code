test_input = "389125467"

input = "952316487"

def parse_input(text):
    return list(map(int, text))

def move(cups, cup):
    N = len(cups)
    idx = cups.index(cup)
    next_cup = cups[(idx + 4) % len(cups)]
    next1, next2, next3 = cups[(idx + 1) % N], cups[(idx + 2) % N], cups[(idx + 3) % N]
    cups.remove(next1)
    cups.remove(next2)
    cups.remove(next3)
    dest = cup
    while True:
        dest = (dest - 1) % (N + 1)
        if dest in [0, next1, next2, next3, cup]:
            continue
        for i in range(len(cups)):
            if cups[i] == dest:
                cups.insert(i + 1, next1)
                cups.insert(i + 2, next2)
                cups.insert(i + 3, next3)
                return next_cup

def run(cups, n, verbose=False):
    cup = cups[0]
    for i in range(1, n+1):
        if verbose:
            print("Cup", cup)
            print("Move", i, cups)
        cup = move(cups, cup)
    if verbose:
        print("Cup", cup)
        print("Move", i + 1, cups)

def canonical(cups):
    idx = cups.index(1)
    res = []
    for i in range(1, len(cups)):
        res.append(cups[(idx + i) % len(cups)])
    return ''.join(map(str, res))

print("Day 23")
print("Part 1")
print("Test input")
test_cups = parse_input(test_input)
test_cups2 = test_cups.copy()
run(test_cups2, 10, verbose=True)
print(test_cups2)
run(test_cups, 100)
print(test_cups)
print(canonical(test_cups))

print("Puzzle input")
cups = parse_input(input)
run(cups, 100)
print(cups)
print(canonical(cups))
