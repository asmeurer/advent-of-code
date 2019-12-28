from collections import defaultdict

def parse_input(I):
    lines = I.strip().splitlines()
    A = defaultdict(int)
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                A[(0, y, x)] = 1
    return A

def run(A, n):
    for i in range(n):
        A = step(A)
    return A

def step(A):
    B = defaultdict(int)
    # Initialize all relevant spaces
    for (l, i, j), x in A.copy().items():
        for adjl, adji, adjj in adj(l, i, j):
            A[adjl, adji, adjj]

    for (l, i, j), x in A.copy().items():
        alive = 0
        for adjl, adji, adjj in adj(l, i, j):
            alive += A[adjl, adji, adjj]
        if A[l, i, j] == 0 and alive in [1, 2]:
            B[l, i, j] = 1
        elif A[l, i, j] == 1:
            if alive != 1:
                B[l, i, j] = 0
            else:
                B[l, i, j] = 1
    return B

def adj(l, i, j):
    for adji, adjj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if adji == -1:
            yield (l - 1, 1, 2)
        elif adji >= 5:
            yield (l - 1, 3, 2)
        elif adjj == -1:
            yield (l - 1, 2, 1)
        elif adjj >= 5:
            yield (l - 1, 2, 3)
        elif (adji, adjj) == (2, 2):
            if (i, j) == (1, 2):
                for adjj_ in range(5):
                    yield (l + 1, 0, adjj_)
            if (i, j) == (2, 1):
                for adji_ in range(5):
                    yield (l + 1, adji_, 0)

            if (i, j) == (2, 3):
                for adji_ in range(5):
                    yield (l + 1, adji_, 4)
            if (i, j) == (3, 2):
                for adjj_ in range(5):
                    yield (l + 1, 4, adjj_)
        else:
            yield (l, adji, adjj)

D = {
    0: '.',
    1: '#',
    }

def print_bugs(A):
    minl = min(A.keys(), key=lambda x: x[0])[0]
    maxl = min(A.keys(), key=lambda x: x[0])[1]
    for l in range(minl, maxl+1):
        print("Level", l)
        for y in range(5):
            for x in range(5):
                if (x, y) == (2, 2):
                    print('?', end='')
                else:
                    print(D[A[l, y, x]], end='')
            print()

test_input = """
....#
#..#.
#..##
..#..
#....
"""

input = """
.##..
##.#.
##.##
.#..#
#.###
"""

def main():
    print(list(adj(0, 1, 3)))
    A = parse_input(test_input)
    print("Day 26 part 2 test input")
    print("0 steps")
    print_bugs(A)
    print()
    print("1 step")
    print_bugs(step(A))
    print()
    A = run(A, 10)
    print("10 steps")
    print_bugs(A)
    print(sum(A.values()), "bugs")

    print("Day 26 part 1")
    A = parse_input(input)
    A = run(A, 200)
    print_bugs(A)
    print(sum(A.values()), "bugs")

if __name__ == '__main__':
    main()
