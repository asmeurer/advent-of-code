test_input = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

test_input2 = """
11111
19991
19191
19991
11111
"""

input = """
4472562264
8631517827
7232144146
2447163824
1235272671
5133527146
6511372417
3841841614
8621368782
3246336677
"""

import itertools

import numpy as np

def parse_input(data):
    return np.array([[int(i) for i in line] for line in
                     data.strip().splitlines()])

def step(a, debug=False):
    a = a.copy()
    a += 1
    flash = np.zeros(a.shape, dtype=bool)

    while True:
        if not np.any((a > 9) & ~flash):
            break
        this_flash = (a > 9)
        flash |= this_flash
        if debug:
            print("flash")
            print(np.array(flash, dtype=int))
        B = np.full((8, *a.shape), False)
        i = -1
        for idx in itertools.product(*[(slice(None), slice(1, None), slice(None, -1))]*2):
            if idx == (slice(None), slice(None)):
                continue
            i += 1
            B[i][::-1,::-1][idx] = this_flash[idx][::-1,::-1]

        surrounding = np.sum(B, axis=0)
        if debug:
            print("surrounding")
            print(surrounding)
        a += surrounding
        a[flash] = 0
        if debug:
            print("a")
            print(a)

    return a

def do_steps(a, n):
    flashes = 0
    for i in range(n):
        a = step(a)
        flashes += np.sum(a == 0)
    return flashes

def find_sync(a):
    n = 0
    while True:
        if np.all(a == 0):
            return n
        n += 1
        a = step(a)

print("Day 11")
print("Part 1")
print("Test input")
test_a = parse_input(test_input)
test_a2 = parse_input(test_input2)
print("Test 1 step 1")
step(test_a2, debug=True)
print("Test 1 step 2")
print(step(step(test_a2), debug=True))

print("Test 2 step 1")
test_a = step(test_a)
print(test_a)
print(np.sum(test_a == 0), "flashes")
print("Test 2 step 2")
test_a = step(test_a)
print(test_a)
print(np.sum(test_a == 0), "flashes")

test_a = parse_input(test_input)
print("Test 2 10 steps")
test_flashes10 = do_steps(test_a, 10)
print(test_flashes10)

print("Test 2 100 steps")
test_flashes100 = do_steps(test_a, 100)
print(test_flashes100)

print("Puzzle input")
a = parse_input(input)
flashes100 = do_steps(a, 100)
print(flashes100)

print("Part 2")
print("Test input")
test_a = parse_input(test_input)
for i in range(192):
    test_a = step(test_a)
print("Test step 193")
test_a = step(test_a)
print(test_a)
print("Test step 194")
test_a = step(test_a)
print(test_a)
print("Test step 195")
test_a = step(test_a)
print(test_a)

test_a = parse_input(test_input)
print(find_sync(test_a))

print("Puzzle input")
a = parse_input(input)
print(find_sync(a))
