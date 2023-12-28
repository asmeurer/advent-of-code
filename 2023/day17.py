test_input = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""".strip()

puzzle_input = open('day17_input').read().strip()

import heapq
from collections import defaultdict

import numpy as np

def parse_input(input):
    return np.array([list(map(int, line)) for line in input.splitlines()])

def get_neighbors(node, map, path):
    x, y = node
    plusx, plusy, minusx, minusy = [True]*4

    # Avoid runs in the same direction of greater than 3
    if len(path) >= 4:
        if path[-1][0] == path[-2][0] == path[-3][0] == path[-4][0]:
            plusy = False
            minusy = False
        if path[-1][1] == path[-2][1] == path[-3][1] == path[-4][1]:
            plusx = False
            minusx = False

    if x == 0:
        minusx = False
    if x == map.shape[0]-1:
        plusx = False
    if y == 0:
        minusy = False
    if y == map.shape[1]-1:
        plusy = False

    # Don't allow the path to go back on itself
    if len(path) >= 2:
        if path[-2][0] == path[-1][0] - 1:
            minusx = False
        if path[-2][0] == path[-1][0] + 1:
            plusx = False
        if path[-2][1] == path[-1][1] - 1:
            minusy = False
        if path[-2][1] == path[-1][1] + 1:
            plusy = False

    if plusx:
        yield (x+1, y)
    if plusy:
        yield (x, y+1)
    if minusx:
        yield (x-1, y)
    if minusy:
        yield (x, y-1)

def dfs(start, end, map):
    # I'm not sure if we can necessarily rule out the same cell being visited
    # twice because of the three in a row rule, so start with a min cost of a
    # simple (valid) path
    min_cost = np.sum(np.diagonal(map)) + np.sum(np.diagonal(map, 1)) - map[0, 0]

    def _dfs(node, path):
        # print_path(map, path)
        cost = sum(map[i] for i in path) + map[node]
        if node == end:
            nonlocal min_cost
            if cost < min_cost:
                print('Found path with cost', cost)
                print_path(map, path + [node])
            min_cost = min(min_cost, cost)
            return
        if cost > min_cost:
            # print('Pruning')
            # print_path(map, path)
            return
        path.append(node)
        for neighbor in sorted(get_neighbors(node, map, path), key=map.__getitem__):
            _dfs(neighbor, path)
        path.pop()

    path = []
    _dfs(start, path)

    print_path(map, path)
    return min_cost

# Taken from 2021/day15
def astar(start, end, map):
    openset = []
    heapq.heappush(openset, start)

    camefrom = {}

    gscore = defaultdict(lambda: np.inf)
    gscore[start] = 0

    fscore = defaultdict(lambda: np.inf)
    fscore[start] = 0

    while openset:
        current = heapq.heappop(openset)
        path = reconstruct_path(current, camefrom)
        if current == end:
            return path

        for neighbor in get_neighbors(current, map, path):
            tenative_gscore = gscore[current] + map[neighbor]
            if tenative_gscore < gscore[neighbor]:
                camefrom[neighbor] = current
                gscore[neighbor] = tenative_gscore
                # h_neighbor = sum(map[i] for i in path) + map[neighbor]
                h_neighbor = 0
                # print_path(map, path + [neighbor])
                # print()
                fscore[neighbor] = tenative_gscore + h_neighbor
                if neighbor not in openset:
                    heapq.heappush(openset, neighbor)

    raise ValueError("Could not find a path")

def reconstruct_path(current, camefrom):
    total_path = [current]
    while current in camefrom:
        current = camefrom[current]
        total_path.insert(0, current)
    return total_path

def print_path(map, path):
    dpath = {}
    for i in range(1, len(path)):
        a, b = path[i-1], path[i]
        if b[0] == a[0] - 1:
            dpath[b] = '^'
        elif b[0] == a[0] + 1:
            dpath[b] = 'v'
        elif b[1] == a[1] - 1:
            dpath[b] = '<'
        elif b[1] == a[1] + 1:
            dpath[b] = '>'

    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if (i, j) in dpath:
                print(dpath[i, j], end='')
            else:
                print('.', end='')
        print()
    print()

def part1(map):
    x, y = map.shape
    start = (0, 0)
    end = (x-1, y-1)
    path = dfs(start, end, map)
    print_path(map, path)
    return sum(map[i] for i in path[1:])

if __name__ == '__main__':
    print("Day 17")
    print("Part 1")
    print("Test input")
    test_map = parse_input(test_input)
    # print(part1(test_map))
    print("Puzzle input")
    puzzle_map = parse_input(puzzle_input)
    print(part1(puzzle_map))
