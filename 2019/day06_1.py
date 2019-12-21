def create_graph(input):
    g = {}
    for line in input.strip().splitlines():
        a, b = line.split(')')
        g[b] = a
    return g

def length(g, i):
    N = 0
    while i != 'COM':
        i = g[i]
        N += 1
    return N

def count(g):
    return sum([length(g, i) for i in g])

test_input = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

with open('day06-input') as f:
    input = f.read()

if __name__ == '__main__':
    print("Test input")
    test_G = create_graph(test_input)
    print(count(test_G))

    print("Part 1")
    G = create_graph(input)
    print(count(G))
