from itertools import combinations

import numpy as np

def step(P, V):
    delta = np.zeros((V.shape), dtype=np.int64)
    for i, j in combinations(range(P.shape[0]), 2):
        # Apply gravity
        for coord in range(3):
            if P[i][coord] < P[j][coord]:
                delta[i][coord] += 1
                delta[j][coord] -= 1
            elif P[i][coord] > P[j][coord]:
                delta[i][coord] -= 1
                delta[j][coord] += 1

    V = V + delta
    P = P + V
    return P, V

def run_steps(P, n, print_=False):
    V = np.zeros(P.shape, dtype=np.int64)
    for i in range(n):
        P, V = step(P, V)
        if print_:
            print("Iteration", i)
            print("Positions\n", P)
            print("Velocities\n", V)
            print()
    return P, V

def parse_input(I):
    I = I.strip().splitlines()
    P = np.zeros((len(I), 3), dtype=np.int64)
    for i in range(len(I)):
        line = I[i].strip('<>').split(', ')
        coords = [int(i[2:]) for i in line]
        P[i] = coords

    return P

def compute_energy(P, V):
    return np.sum(np.sum(abs(P), axis=1)*np.sum(abs(V), axis=1))

test_input1 = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""

test_input2 = """
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
"""

input = """
<x=16, y=-8, z=13>
<x=4, y=10, z=10>
<x=17, y=-5, z=6>
<x=13, y=-3, z=0>
"""

if __name__ == '__main__':
    print("Day 12, part, test 1")
    P = parse_input(test_input1)
    P, V = run_steps(P, 10, print_=True)
    print(compute_energy(P, V))

    print("Day 12, part 1, test 2")
    P = parse_input(test_input2)
    P, V = run_steps(P, 100, print_=True)
    print(compute_energy(P, V))

    print("Day 12, part 1")
    P = parse_input(input)
    P, V = run_steps(P, 1000)
    print(compute_energy(P, V))
