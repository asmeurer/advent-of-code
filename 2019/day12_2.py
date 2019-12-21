from itertools import combinations

import numpy as np
from numba import njit, prange
from sympy import ilcm

combos = np.array(list(combinations(range(4), 2)))

@njit
def step(P, V):
    delta = np.zeros((V.shape), dtype=np.int64)
    for c in range(combos.shape[0]):
        i, j = combos[c][0], combos[c][1]
        # Apply gravity
        if P[i] < P[j]:
            delta[i] += 1
            delta[j] -= 1
        elif P[i] > P[j]:
            delta[i] -= 1
            delta[j] += 1

    V = V + delta
    P = P + V
    return P, V

@njit()
def run_steps(Px, Py, Pz):
    Vx = np.zeros(Px.shape, dtype=np.int64)
    Vy = np.zeros(Py.shape, dtype=np.int64)
    Vz = np.zeros(Pz.shape, dtype=np.int64)
    first_Px = Px.copy()
    first_Py = Py.copy()
    first_Pz = Pz.copy()
    repeatx = repeaty = repeatz = n = 0
    while repeatx == 0 or repeaty == 0 or repeatz == 0:
        for coord in range(3):
            if coord == 0 and repeatx == 0:
                Px, Vx = step(Px, Vx)
                if np.all(Px == first_Px) and np.all(Vx == 0):
                    repeatx = n
            elif coord == 1 and repeaty == 0:
                Py, Vy = step(Py, Vy)
                if np.all(Py == first_Py) and np.all(Vy == 0):
                    repeaty = n
            elif coord == 2 and repeatz == 0:
                Pz, Vz = step(Pz, Vz)
                if np.all(Pz == first_Pz) and np.all(Vz == 0):
                    repeatz = n
        n += 1
    return (repeatx, repeaty, repeatz)

def parse_input(I):
    I = I.strip().splitlines()
    P = np.zeros((len(I), 3), dtype=np.int64)
    for i in range(len(I)):
        line = I[i].strip('<>').split(', ')
        coords = [int(i[2:]) for i in line]
        P[i] = coords

    return P

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
    print("Day 12, part 2, test 1")
    P = parse_input(test_input1)
    repeatx, repeaty, repeatz = run_steps(P[:, 0], P[:, 1], P[:, 2])
    print(repeatx, repeaty, repeatz)
    print(ilcm(repeatx+1, repeaty+1, repeatz+1))

    print("Day 12, part 2, test 2")
    P = parse_input(test_input2)
    repeatx, repeaty, repeatz = run_steps(P[:, 0], P[:, 1], P[:, 2])
    print(repeatx, repeaty, repeatz)
    print(ilcm(repeatx+1, repeaty+1, repeatz+1))

    print("Day 12, part 2")
    P = parse_input(input)
    repeatx, repeaty, repeatz = run_steps(P[:, 0], P[:, 1], P[:, 2])
    print(repeatx, repeaty, repeatz)
    print(ilcm(repeatx+1, repeaty+1, repeatz+1))
