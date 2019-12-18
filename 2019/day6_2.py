from day6_1 import input, create_graph, length

def jumps(g):
    you_len = length(g, 'YOU')
    san_len = length(g, 'SAN')
    you_planet = g['YOU']
    san_planet = g['SAN']
    N = 0
    while True:
        if you_planet == san_planet:
            break
        if you_len > san_len:
            you_planet = g[you_planet]
            you_len -= 1
        else:
            san_planet = g[san_planet]
            san_len -= 1
        N += 1
    return N

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
K)YOU
I)SAN
"""

if __name__ == '__main__':
    print("Test input")
    test_G = create_graph(test_input)
    print(jumps(test_G))

    print("Part 1")
    G = create_graph(input)
    print(jumps(G))
