test_input = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

input = """
Player 1:
39
15
13
23
12
49
36
44
8
21
28
37
40
42
6
47
2
38
18
31
20
10
16
43
5

Player 2:
29
26
19
35
34
4
41
11
3
50
33
22
48
7
17
32
27
45
46
9
25
30
1
24
14
"""

def parse_input(text):
    player1, player2 = text.strip().split('\n\n')
    player1 = list(map(int, player1.splitlines()[1:]))
    player2 = list(map(int, player2.splitlines()[1:]))
    return player1, player2

def round(player1, player2):
    card1, card2 = player1.pop(0), player2.pop(0)
    if card1 > card2:
        player1.extend([card1, card2])
    else:
        player2.extend([card2, card1])

def play(player1, player2):
    while player1 and player2:
        round(player1, player2)

    return player1, player2

def score(cards):
    return sum(i*card for i, card in enumerate(reversed(cards), 1))

print("Day 22")
print("Part 1")
print("Test input")
test_player1, test_player2 = parse_input(test_input)
print(test_player1, test_player2)
round(test_player1, test_player2)
print("Round 1")
print(test_player1, test_player2)
print(play(test_player1, test_player2))
print(score(test_player1 or test_player2))

print("Puzzle input")
player1, player2 = parse_input(input)
print(player1, player2)
round(player1, player2)
print("Round 1")
print(player1, player2)
print(play(player1, player2))
print(score(player1 or player2))
