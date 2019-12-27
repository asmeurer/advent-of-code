import numpy as np

def parse_input(I):
    lines = I.strip().splitlines()
    A = np.zeros((len(lines), len(lines[0])), dtype=np.int64)
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                A[y][x] = 1
    return A

def toint(A):
    res = 0
    for i, x in enumerate(A.flatten()):
        res += 2**i*x
    return res

def run(A):
    seen = {toint(A)}
    while True:
        A = step(A)
        i = toint(A)
        if i in seen:
            return i
        seen.add(i)

def step(A):
    B = A.copy()
    for (i, j), x in np.ndenumerate(A):
        alive = 0
        for adji, adjj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if adji == -1 or adjj == -1:
                continue
            if adji >= A.shape[0] or adjj >= A.shape[1]:
                continue
            alive += A[adji, adjj]
        if A[i, j] == 0 and alive in [1, 2]:
            B[i, j] = 1
        elif A[i, j] == 1 and alive != 1:
            B[i, j] = 0
    return B



test_input = """
....#
#..#.
#..##
..#..
#....
"""

test_input_answer = """
.....
.....
.....
#....
.#...
"""

input = """
.##..
##.#.
##.##
.#..#
#.###
"""

def main():
    A = parse_input(test_input)
    print("Day 26 test input")
    print("Should give 2129920")
    print(toint(parse_input(test_input_answer)))

    print(run(A))

    print("Day 26 part 1")
    A = parse_input(input)
    print(run(A))

if __name__ == '__main__':
    main()
