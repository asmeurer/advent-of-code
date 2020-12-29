test_input = "389125467"

input = "952316487"

import sys

import numpy as np

from numba import njit

def parse_input(text):
    return np.array([list(map(int, text)), list(range(1, len(text))) + [0]]).T

def extend_cups(cups, N):
    n = cups.shape[0]
    extended = np.array(list(range(n+1, N + 1)))
    res = np.zeros((N, 2), dtype=int)
    res[:n] = cups
    res[n-1][1] = n
    res[n:, 0] = extended
    res[n:N-1, 1] = extended[:N - n - 1]
    res[N-1][1] = 0
    return res

@njit
def move(cups, cup_idx):
    N = len(cups)
    cup, next1_idx = cups[cup_idx]
    next1, next1_idx = next(cups, cup_idx)
    next2, next2_idx = next(cups, next1_idx)
    next3, next3_idx = next(cups, next2_idx)
    next4, next4_idx = next(cups, next3_idx)

    cups[cup_idx][1] = next4_idx

    dest = cup
    while True:
        dest = (dest - 1) % (N + 1)
        if dest not in [0, next1, next2, next3, cup]:
            break

    dest_idx, dest_next = index(cups, dest)

    # Insert next1, next2, next3 after dest
    cups[dest_idx][1] = next1_idx
    cups[next3_idx][1] = dest_next
    return next4_idx

@njit
def next(cups, i):
    idx = cups[i][1]
    return cups[idx][0], idx

@njit
def index(cups, dest):
    for dest_idx, (c, dest_next) in enumerate(cups):
        if c == dest:
            break
    return dest_idx, dest_next

@njit
def run(cups, n, verbose=0):
    cup_idx = 0
    for i in range(1, n+1):
        if verbose == 1:
            print("Cup", cups[cup_idx])
            print("Move", i, cups)
        if verbose == 2:
            if i % 1000 == 0:
                print(i, n, i/n)
        cup_idx = move(cups, cup_idx)
    if verbose == 1:
        print("Cup", cups[cup_idx])
        print("Move", i + 1, cups)

def canonical(cups):
    c = 1
    idx, _ = index(cups, c)
    res = np.zeros(len(cups), dtype=int)
    for i in range(len(cups)):
        res[i] = c
        c, idx = next(cups, idx)

    return ''.join(map(str, res[1:]))

def main():
    print("Day 23")
    print("Part 1")
    print("Test input")
    test_cups = parse_input(test_input)
    print(test_cups)
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

    print("Part 2")
    N = 1_000_000
    if sys.argv[1] == 'test':
        print("Test input")
        test_cups = parse_input(test_input)
        print(extend_cups(test_cups, 20))
        test_cups2 = extend_cups(test_cups, N)
        # run(test_cups2, 20, verbose=1)
        run(test_cups2, 10*N, verbose=2)
        print(test_cups2[:100])
        idx, n = index(test_cups2, 1)
        test_star1, n = next(test_cups2, idx)
        test_star2, n = next(test_cups2, n)
        print(test_star1, test_star2)
        print(test_star1*test_star2)
    else:
        print("Puzzle input")
        cups = parse_input(input)
        print(extend_cups(cups, 20))
        cups2 = extend_cups(cups, N)
        # run(cups2, 20, verbose=1)
        run(cups2, 10*N, verbose=2)
        print(cups2[:100])
        idx, n = index(cups2, 1)
        star1, n = next(cups2, idx)
        star2, n = next(cups2, n)
        print(star1, star2)
        print(star1*star2)

if __name__ == '__main__':
    main()
