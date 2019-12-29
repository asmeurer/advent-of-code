import sys
from collections import defaultdict

import numpy as np

def asarray(I):
    lines = I.splitlines()
    return np.array(lines, "S").view("S1").reshape((len(lines), -1))

def make_graph(A):
    graph = defaultdict(list)
    connections = defaultdict(list)
    for (i, j), x in np.ndenumerate(A):
        if x == b'.':
            for i_, j_ in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if A[i_, j_] == b'.':
                    graph[i, j].append((i_, j_))

                if A[i_, j_].isalpha():
                    if i_ == i - 1:
                        name = A[i - 2, j] + A[i - 1, j]
                    elif i_ == i + 1:
                        name = A[i + 1, j] + A[i + 2, j]
                    elif j_ == j - 1:
                        name = A[i, j - 2] + A[i, j - 1]
                    elif j_ == j + 1:
                        name = A[i, j + 1] + A[i, j + 2]
                    else:
                        raise RuntimeError("Unexpected i, j: %s, %s" % (i, j))
                    if name == b'AA':
                        start = i, j
                    elif name == b'ZZ':
                        end = i, j
                    else:
                        connections[name].append((i, j))

    for a, b in connections.values():
        graph[a].append(b)
        graph[b].append(a)

    return graph, start, end

def bfs(tree, path):
    for item in tree[path[-1]]:
        if item in path:
            continue
        yield from bfs(tree, path + [item])
        yield path + [item]

def find_paths(graph, start, end):
    for path in bfs(graph, [start]):
        if path[-1] == end:
            yield path

def shortest_path(graph, start, end):
    return len(min(find_paths(graph, start, end), key=len)) - 1

with open('day20-test-input-1') as f:
    test_input_1 = f.read()

with open('day20-test-input-2') as f:
    test_input_2 = f.read()

with open('day20-input') as f:
    input = f.read()

def main():
    print("Day 20 part 1 test input 1")
    print("Should give 23")
    A = asarray(test_input_1)
    graph, start, end = make_graph(A)
    # print(start)
    # print(end)
    # print(graph)
    # path = next(find_paths(graph, start, end))
    # print(path)
    # print(len(path) - 1)
    print(shortest_path(graph, start, end))

    print("Day 20 part 1 test input 2")
    print("Should give 58")
    A = asarray(test_input_2)
    graph, start, end = make_graph(A)
    # print(start)
    # print(end)
    # print(graph)
    # paths = find_paths(graph, start, end)
    # for path in paths:
    #     # print(path)
    #     print(len(path) - 1)
    print(shortest_path(graph, start, end))

    print("Day 20 part 1")
    A = asarray(input)
    graph, start, end = make_graph(A)
    sys.setrecursionlimit(2000)
    print(shortest_path(graph, start, end))

if __name__ == '__main__':
    main()
