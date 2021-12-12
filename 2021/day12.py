test_input1 = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

test_input2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

test_input3 = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

input = """
start-co
ip-WE
end-WE
le-ls
wt-zi
end-sz
wt-RI
wt-sz
zi-start
wt-ip
YT-sz
RI-start
le-end
ip-sz
WE-sz
le-WE
le-wt
zi-ip
RI-zi
co-zi
co-le
WB-zi
wt-WE
co-RI
RI-ip
"""

from collections import defaultdict

def parse_input(data):
    lines = data.strip().splitlines()
    G = defaultdict(list)
    for line in lines:
        a, b = line.split('-')
        G[a].append(b)
        G[b].append(a)

    return dict(G)

def walk(G, here='start', path=()):
    for cave in G[here]:
        if cave == 'end':
            yield path + (here, 'end')
        elif cave.isupper() or cave not in path:
            yield from walk(G, here=cave, path=path+(here,))


print("Day 12")
print("Part 1")
print("Test input")
test_graph1 = parse_input(test_input1)
print(test_graph1)
for w in walk(test_graph1):
    print(w)
print("Test graph 1", len(list(walk(test_graph1))))

test_graph2 = parse_input(test_input2)
print("Test graph 2", len(list(walk(test_graph2))))

test_graph3 = parse_input(test_input3)
print("Test graph 3", len(list(walk(test_graph3))))

print("Puzzle input")
graph = parse_input(input)
print(len(list(walk(graph))))

# print("Part 2")
# print("Test input")

# print("Puzzle input")
