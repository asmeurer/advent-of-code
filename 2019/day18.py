from collections import defaultdict
from random import shuffle

from numba import njit

from day15_1 import luby

import numpy as np

def asarray(I):
    lines = I.splitlines()
    return np.array(lines, "S").view("S1").reshape((len(lines), -1))

def make_graph(A, cache={}):
    s = A.tostring()
    if s in cache:
        return cache[s]
    graph = defaultdict(set)
    keys = {}

    for (i, j), x in np.ndenumerate(A):
        if x == b'.' or x == b'@':
            for i_, j_ in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if A[i_, j_] == b'.' or A[i_, j_].isalpha() or A[i_, j_] == b'@':
                    graph[i, j].add((i_, j_))
        if x.islower():
            keys[x] = (i, j)
        # if x.isupper():
        #     keys[x] = (i, j)
        if x == b'@':
            start = (i, j)

    cache[s] = (graph, keys, start)
    return graph, keys, start

# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
# @njit
def dijkstra(graph, start, end, cache={}):
    k = (frozenset((key, frozenset(value)) for key, value in graph.items()), frozenset([start, end]))
    if k in cache:
        return cache[k]
    unvisited = set.union(*graph.values())
    dist = {node: float('inf') for node in unvisited}
    dist[start] = 0
    prev = {}

    while unvisited:
        current = min(unvisited, key=lambda i: dist[i])
        unvisited.remove(current)
        if current == end:
            break
        for node in graph[current]:
            if node in unvisited:
                alt = dist[current] + 1
                if alt < dist[node]:
                    dist[node] = alt
                    prev[node] = current
    else:
        return False

    path = []
    while current != start:
        path.insert(0, current)
        if current not in prev:
            return False
        current = prev[current]

    cache[k] = path
    return path

class MaxIteration(Exception):
    pass

def backtrack(A):
    minpath = float('inf')
    def _backtrack(A, depth='', l=0):
        nonlocal minpath
        nonlocal iters
        if l >= minpath:
            # print("Skipping")
            return

        if iters >= max_iters:
            print('\r', end='')
            raise MaxIteration

        graph, keys, start = make_graph(A)

        K = list(keys)
        shuffle(K)

        if not keys:
            if l < minpath:
                print("New minimum:", l)
                minpath = l
            yield []
        for k in K:
            print('\r%s' % iters, end='')
            iters += 1
            # print(iters, max_iters, depth + k.decode('utf-8'), ''.join([i.decode('utf-8') for i
            #                                               in sorted(set(keys) -
            #                                                         {k})]), minpath)
            path = dijkstra(graph, start, keys[k])
            if path:
                B = A.copy()
                B[B == k.upper()] = b'.'
                B[B == b'@'] = b'.'
                B[B == k] = b'@'
                for p in _backtrack(B, depth=depth+k.decode('utf-8'),
                                    l=l+len(path)):
                    yield path + p

    for i in luby():
        try:
            iters = 0
            max_iters = i*200
            print("Max iters:", max_iters, "Best:", minpath)
            yield from _backtrack(A)
        except MaxIteration:
            pass
        else:
            return

def print_puzzle(A):
    for x in range(A.shape[0]):
        for y in range(A.shape[1]):
            print(A[x, y].decode('utf-8'), end='')
        print()

def find_min(A):
    return len(min(backtrack(A), key=len))

test_input_1 = """\
#########
#b.A.@.a#
#########\
"""

test_input_2 = """\
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################\
"""

test_input_3 = """\
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################\
"""

test_input_4 = """\
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################\
"""

test_input_5 = """\
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################\
"""

with open('day18-input') as f:
    input = f.read()

def main():
    print("Day 18 part 1 test input 1")
    A = asarray(test_input_1)
    graph, keys, start = make_graph(A)
    print(test_input_1)
    print(graph)
    print(keys)
    print(start)
    for k in keys:
        print(k, dijkstra(graph, start, keys[k]))
    for path in backtrack(A):
        print(len(path), path)
    print("Should give 8")
    print(find_min(A))

    print("Day 18 part 1 test input 2")
    A = asarray(test_input_2)
    for path in backtrack(A):
        print(len(path), path)
    print("Should give 86")
    print(find_min(A))

    print("Day 18 part 1 test input 3")
    A = asarray(test_input_3)
    print("Should give 132")
    print(find_min(A))

    print("Day 18 part 1 test input 4")
    A = asarray(test_input_4)
    graph, keys, start = make_graph(A)
    for k in keys:
        print(k, dijkstra(graph, start, keys[k]))
    print("Should give 136")
    # print(find_min(A))

    print("Day 18 part 1 test input 5")
    A = asarray(test_input_5)
    print("Should give 81")
    print(find_min(A))

    print("Day 18 part 1")
    A = asarray(input)
    print(find_min(A))

if __name__ == '__main__':
    main()
