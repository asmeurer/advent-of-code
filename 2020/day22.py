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

test_input2 = """
Player 1:
43
19

Player 2:
2
29
14
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

def round2(player1, player2, prev_games):
    card1, card2 = player1[0], player2[0]
    end = False
    if (player1, player2) in prev_games:
        winner = 1
        end = True
    else:
        prev_games.add((player1, player2))
        if card1 <= len(player1[1:]) and card2 <= len(player2[1:]):
            sub1, sub2 = play2(player1[1:1+card1], player2[1:1+card2])
            winner = 1 if sub1 else 2
        else:
            winner = 1 if card1 > card2 else 2

    if winner == 1:
        return player1[1:] + (card1, card2), player2[1:], end
    else:
        return player1[1:], player2[1:] + (card2, card1), end

def play2(player1, player2):
    prev_games = set()
    while player1 and player2:
        player1, player2, end = round2(player1, player2, prev_games)
        if end:
            break
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

print("Part 2")
print("Test input")
test_player1, test_player2 = map(tuple, parse_input(test_input))
test_prev_games = set()
# print(round2(test_player1, test_player2, test_prev_games))
# print(round2(*round2(test_player1, test_player2, test_prev_games), test_prev_games))
# print(round2(*round2(*round2(test_player1, test_player2, test_prev_games),
#                      test_prev_games), test_prev_games))
test_player1_final, test_player2_final = play2(test_player1, test_player2)
print(test_player1_final, test_player2_final)
print(score(test_player1_final or test_player2_final))

print("Test input 2 (should not infinitely recurse)")
test2_player1, test2_player2 = map(tuple, parse_input(test_input2))
test2_player1_final, test2_player2_final = play2(test2_player1, test2_player2)
print(test2_player1_final, test2_player2_final)

print("Puzzle input")
player1, player2 = map(tuple, parse_input(input))
player1_final, player2_final = play2(player1, player2)
print(player1_final, player2_final)
print(score(player1_final or player2_final))
