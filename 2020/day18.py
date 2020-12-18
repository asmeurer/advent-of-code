test_inputs = {
    "1 + 2 * 3 + 4 * 5 + 6": 71,
    "1 + (2 * 3) + (4 * (5 + 6))": 51,
    "2 * 3 + (4 * 5)": 26,
    "5 + (8 * 3 + 9 + 3 * 4 * 3)": 437,
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))": 12240,
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2": 13632,
}

test_inputs2 = {
    "1 + 2 * 3 + 4 * 5 + 6": 231,
    "1 + (2 * 3) + (4 * (5 + 6))": 51,
    "2 * 3 + (4 * 5)": 46,
    "5 + (8 * 3 + 9 + 3 * 4 * 3)": 1445,
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))": 669060,
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2": 23340,
}

input = """
5 + 8 * ((6 * 5 * 8 + 5 + 8) * 7 + 3)
6 * 7 + 7 * (9 * 6 + 6 + 4 * 6) * 5 * 4
((3 * 8 + 7) * 3 * 8 * 8 * 4 * 2) * 8
((4 + 5 * 8 + 6 * 5) * 3 * 4 * 9 * 3 + (9 * 8)) + 2 * 7
(6 + 5) * 6
3 * 4 + 3 + (6 * 3 + (5 + 7 * 7 + 6) * 9)
9 * 6 * (5 + 6) + (3 + 8 * 3 * 4 + 8) + 2 * 3
7 * ((4 * 7 + 7) + 7) + 9 + 2 + 2
5 + 8 + 5 + (8 * 8 * 5) * (5 + (6 * 2 + 4 + 6) + 9 * 6 + 6 + (5 + 6)) * 4
3 * (7 * (6 + 8 * 4 + 7 + 2)) * 9 * (8 * 9) * (6 + 3) + 7
(8 + 4 * (2 * 9) + 6 + 6 + 3) + 4
4 + 6 + (3 + 8 * 2 * 6 * 7 + 3)
3 * 5 + (8 * 2 * (7 * 6 + 8 * 9 * 6)) * ((9 * 3 + 2 * 9 + 2 * 4) * 3) * 7 * 2
(3 * 3 * (2 * 6 * 3) + 9 + (9 * 8 * 9 * 2) + 4) + 6 * 7 + 9 * 7 * ((9 * 8 + 8) + 4)
(5 + 7 * 5 * 8 * 8) * (7 * (6 + 4 * 6 * 8) * 5 * (3 * 7 * 3 * 2 + 2 * 6) * 3 + 3) + 8 + (3 + (7 * 7 + 3))
6 + 4 * (2 + 6 + 7 + 8) * 3 + (2 + 3) + (8 * (8 + 8) * 6)
(9 + 3) * 7 + 4 + 6 * 3 + (2 * 7 + 9 * 7 + 9)
4 + 9 + (7 + 2)
(7 + 4 * 4 * 7 + 2) * 4 * 6 * 5 * (9 + 2)
(7 + 8 * 9 + 9 + 2) + (9 * (9 + 9) + 2) * 5 + 6 + 5 + 9
6 * 2 * 3 * (5 + (4 * 4 * 4 * 2))
2 + 8 + (2 + 8) + 2 * ((7 * 3 * 2 * 2 + 7 * 2) + 3 + 8 + 7) + 3
3 * 6 * 2 + ((4 * 5 * 6) * 6 + 3 + 6) + 4
8 * 8 * (5 + 7 * 6 * 8) * (6 + 5 * 3 * (7 + 8 + 3) * 8 * 2) + 9 * (2 * 9 + 8 * 3)
(5 * 3 + 4) * (3 * 4) * (7 * 7 + 4 + 3)
2 * 8 * (3 * 8 * (5 + 8) * 8 * 2) + 7 + 8
(6 + 5 + 7 + 8 + 2) * (4 * 4)
6 * 8 * 3 * 5
(4 + (9 * 6 * 6 * 8 * 7) + 7 * 5 + (5 + 3 + 4 * 7 + 8) + 7) + 7 + 2 + (6 + 7) * 9
7 + 2 + ((5 + 4 * 6) * 8 + 5) * 7 + 7 + 6
((7 + 9 * 5 * 2) * 8 * 5) * 8
7 * 2 + 4
(9 * 8 * 8 + 8 + (4 + 2 + 5 * 5 * 9) + 3) + (9 * 2 * 8 * 2 * 8) + 7 + 9
5 * 4 * 3 * 2 * 4
3 * 7 + (2 + 3 + 7 + 8) * 4
(3 * (6 + 6 + 3 * 7 + 7 * 8) * 5) + (8 * 8 + 4 * (5 + 4)) * 8 * 4 * 7 * 2
5 * (6 + (4 * 3 + 4 * 2) * 9 * 7 + (9 + 6 + 8)) + 2 + 6 * 3
9 + (9 + 5 + 5) + 9
5 + ((6 * 9 + 9 * 9 + 5 * 6) + 4 + 4) + 6 * 5 + 9 + 3
2 * 8 * (2 * 5 * 4 + 8 + 2 + 5) + 6 + (7 + 7 * 6 + 2 * 6)
8 + (4 + (4 * 9) + 4) * (5 + 5 + (7 + 8 * 2 + 8) + 3 + (3 * 3) + 4)
2 * 6 + 4 + ((2 + 9 * 6 + 7) * 8 + 4 * 2 + (3 + 8 * 2) + 4)
5 * (6 + 9) * (5 + 8 * 3 + 8 * 3 * (6 + 6)) * (8 + 7 + 2 * 9 * 2) + 7
(3 + 7 + 9 * 7 + (3 + 9 * 8 + 2 * 8 * 8) + 8) * 3 * (5 + 6 * 8 + 2 * (4 * 7 * 6) * 2) * 9 * 8
9 + (5 * 4 * 8 + 8) + 7 + (2 * 8 * 4 * 5 * 2) + 2
5 * (4 * (8 * 9 + 7 + 4 + 3 * 2) + (2 * 4 * 7 * 5 + 9 + 2) + (2 + 2 * 9 + 3)) + 8 + 9 + 2 + (4 + 9 + 9 * 2 * (6 * 2 * 4 * 7) + 7)
6 + ((5 * 4 * 6 + 9 * 6 * 3) + 8 * 8) + 2
6 * 5 * 7 * 3 + ((7 * 3) * (7 + 2) + 9 + (9 + 7 * 6 * 6 + 9) * (4 + 8 * 4 + 9)) + 7
3 + 4 + (4 * 7 + 8) + 3 * ((5 * 6) * 6) * (7 + 6 + 9 * 8 + 4 * (4 * 2))
5 * (4 * 5 * (3 * 4 + 4 * 2 * 9 * 8) + 7 * 7) * 7
7 + 8 + (3 * 3 + 2 * (8 * 9) * 5) * 6
3 + 8 * ((6 + 8) * 5 * 3 + 2) * (2 * 5) * 7
4 * 5 + (9 + 8 * (2 * 3 * 4) + 3 * 5) * 9 + 2
4 * ((5 + 6 + 2 + 5 * 3 * 7) * 6) * 7 * 4 + 6 * 4
9 + (9 + 4 * 4 + 7 * 9) + 9 + 2
6 + (8 * (2 + 8 + 6 * 4) * 8) * 7 * 4 * 3 + 9
4 * (5 + (6 * 4 * 8 + 8) * 5 + 6 + 9 * 7) * 6 + 4 * 5
6 * 9 * (6 + 5 * 6 + 2 * (5 + 5 + 8)) + (7 + 7)
(2 * 7 * 4 * 5 * 8 * 2) + 7 + 5 * 8 * 6 + 6
(8 + 3 + 8) * 6 + 8 * (7 * 4 * (5 + 7 + 5 + 7) * 4 + (2 + 2) + 7) + 9
((6 * 7 * 9 * 9 * 2) + (2 + 8 + 2 + 3 + 5) * (8 + 9 + 4 + 3)) + 9 * 3 * 6
5 + 5 * (5 + 2 + 6 + 8 * 8 * 7) + 2 * 2
2 * (4 * (2 + 9 * 4 * 8 + 9) + 3 * 8) + 7
5 + (5 + 2 + (5 * 2 * 7 + 9 * 6)) + 7 + ((4 + 9 * 8 + 2) * 6 + 4 + 2 * 3)
2 + ((2 * 6 + 4 * 8 + 5) * 7 * 4 + 2) + 4
(9 + 8 + 5 * 7 + 5 + 4) + 2 * 3 * 8
9 + ((6 * 6 + 9 + 8 * 9 * 3) + 6) + (9 + 8 * 4) + 7 + 6
2 + (6 + 7 * 2 + 3 * 9 * (4 * 7 + 8 + 2 * 9)) * 9 + 8
9 * 5 + 7 + ((4 + 7 * 6 * 6) * 6 + (3 * 4 + 2 * 7 + 7 + 8) + 9 + (5 * 3 * 4 * 6 * 6 + 7)) * 8 * 6
5 + 5 * 2 * 6 * 2 * 5
6 * 8 + (3 + 9) * 6 * (9 * 8 * 6 * (9 * 6) * (3 * 4)) + (9 + 7 + 6)
3 + 8 * 2 * 9 + 2 * 8
(4 * (3 + 9 + 4 + 9 * 6) * (9 + 6 * 8 + 2 * 7)) + 2
7 * (7 * 8 * (7 + 2 * 5) + 5 + 2) + 4
2 + (4 + 2 + 4 + (8 * 4 + 5 + 6) + 2 * 2) + 9 + 6
((9 + 4 * 7 + 4) * (8 * 3 * 3 + 7 + 8 + 8) + 2 + 7) * 9
5 + 5 + ((8 * 4 * 2) + 3 + 7)
4 + 4 * 7 * 2 + ((6 + 3 * 6) * 5 * (7 * 9 + 8 + 2 * 3))
6 * ((5 * 9 + 4 * 2) + 5 + (8 * 7 * 6 * 3 + 2) * (2 * 2 * 6 * 4 + 2)) * 3
(4 + (5 + 4 + 5) * 7) + (3 * 9 + 5 * 6 + 4) + (5 * 2 + 7 * 7 * 2 + 2)
((5 * 6 * 3) + 9) * (7 * 3 * 3 + (3 + 5 * 4)) + (2 * 8) * 8 + 5
(7 * (2 * 6) + 7 * 3) + 7 + 5
(5 + (8 * 5 + 2 * 8 + 3 * 2) + 5) + 5 * 4 + 5
2 + (5 * 5 + 2 + 7) * (2 * (5 + 3) + 9 * 8 * (5 + 9 * 5 * 7 * 5 + 9))
9 + (7 + 4 + 3 + (3 * 3 + 3 + 6 + 6) * (4 + 6)) * 4 + 8
3 + 4 * ((7 * 4 * 3 * 3 + 7 * 9) + 8 + (3 * 2 * 4 + 3) * 3 + (6 * 7 + 9 + 7 * 8 + 4)) * 6
8 + (7 * (8 + 3 + 5 + 6 + 8) * 9 * (5 + 2 * 4 * 2 + 2) + 6 * 7)
(2 + 5 * 3 * 7 + 3 * (5 * 8 + 3 + 8 * 6)) + 8
5 + 4
8 + 7 + 6 * 5 + 6 + 9
6 * ((4 * 6) * 9 * (5 + 7 + 3 + 5) + 8) + (5 + (3 + 3 * 5 + 7))
(8 + 8 + 8 + 5 * 5 * (3 * 7 * 2 + 5 * 5)) * 6 + 3
4 * (8 + 4 * 3) * (5 * 5 * 6 + 7 + (4 + 4)) + 6 + 9
5 * 7 + 2 + (8 + (8 + 4 + 3 * 9 + 8 + 7) + (4 * 2 * 6 + 2) * 8 + 3 + 9) * (4 * 9 + (5 + 7 + 9)) * 2
3 * (9 * 2 + 6 + 9 + 8) * 2 * 6 * 5
(3 * 7 + (2 * 3 * 2 * 4 + 9)) + (5 * 4 * 7) * 8 * 6 + 9
7 + 8 + 3 * (2 + 7)
9 * (2 * 5 * 5 + 9 + 5 + 2) * (7 * 9 + 3) * 3 * 4
9 * (5 * 5 + 7 * 6) + 8
2 + 9 + (2 + 4 + (3 + 2 + 7 + 7 + 8)) * 3 + 8 + 7
4 * 9 * (4 * (4 * 3 + 2 + 2) * 9 * 9 + 3 + 7) * (5 + 4) * 5 * (7 + 8)
5 * 7 + 2 + 5 * 7 * (9 + 4)
8 + (7 * (6 + 3 + 8 + 6 + 7) * (8 + 8) * 7 * 6 * 4) * 6 + 4
((4 + 6) + 9) + 3 + 8 * (6 + 5) + 6 + 2
7 * (4 * 9 + 5 * 5) + ((4 * 6 + 8) * 8 + 7 * (5 + 6 * 4 * 2 * 2 + 6) * 9 + 8) * 4 + 2 * 3
7 + 7 + (2 * 6 + 2) + 4 * 6
(5 * 2 * 3) * 6
(8 + (4 + 4 + 3 * 5)) * 7 * (8 * 6 * (8 * 9 * 6)) + 2 + (9 + (3 * 5 + 5 * 3) + 5 + 2 * (7 * 3 + 8 + 7 * 3) * 2) * 9
2 * 2 * (8 * (6 + 9 + 6) * 3 * 3 * 8)
9 + 5 + ((9 * 6 + 2 * 5) + (9 + 3) * (5 * 7 * 9 * 4 * 9) + 7) * 2 * 3
8 * (3 + 3 * 3) * 8 + 8
8 * (3 * 4 * (6 + 6 * 4 + 9) * 6) * 9 + 9 * ((2 + 7 + 3) * 5 * (5 + 2 * 4) + (8 * 7 * 9) + (2 + 7 + 2 + 9 * 7 * 4))
4 * 7 * 6 + 4 * 9
8 * 8 * (4 + (2 + 8 * 6) + 8) * ((8 * 7 + 8) * 2 * 2 + (7 * 3 + 9) + 4) + 9
(6 * (4 * 7 * 7 * 5 * 9) * 4 * 8 * 6) * 2
9 + 8 + ((5 * 4) * 3 * 5 + 9) + 8 + 3 + 9
2 * 4 + ((9 * 7) * (8 * 4 * 5 + 6 + 9 + 2) * 8 * 4 + 9) * 8
8 * 4 + ((9 + 6) + 2) * 3 * (7 * 4) + 9
(7 * 6 * 8 * 4 * 2 + 6) * (9 * (3 + 5) + (2 * 6 * 9 * 7 * 2)) * 8 + 2 + 7
7 + 5 * ((9 + 3) + 2 * (6 * 4 + 9 + 2) + 4) * (8 + 3 + 7 * 9 + 3) + 4
7 + ((2 + 8 * 8) + 7 + 8 + (4 * 6 + 7 + 5 * 6 + 6) + 7 + (7 * 4 + 4 * 9 + 6 + 6)) + 6 * 9 * 6 * 7
4 + (5 + 3 * (9 * 6 + 2 * 6) * 5 * (6 * 2)) + (2 * (7 * 4) + (3 + 9 * 6) * 8 * 4 * (8 * 7 * 2 * 4)) + (7 * 3 + 3) * 6
2 + 3 * (8 + (2 + 7 * 3 + 2) + 6) * ((2 + 4) + 3 * 4 * (6 * 4 * 2 * 4 + 7)) + 5
(6 * 3) * 7 + (4 * (7 + 8 * 9) * (9 * 5 + 8 + 4) + 5 * (8 + 9 * 8 * 7 * 9 + 6) + 4)
7 + (8 * 6 + 9 * 7 * 4 * 6)
2 * (3 + 8 + 8 + 3 + 7) * 4 * 6 * (4 + 3 * 5 * 2 * (8 * 8 + 8 + 9 + 7) + 6) * (4 * 9 * 6 + 5)
9 + 6 * 7 * 2 + ((9 + 6 * 3 + 2 * 4 + 3) + 8 + 6 * 8 * 9 + 4)
8 + (2 * 7 + 2 * (7 * 3 + 7 * 2 * 2 * 8) + (7 * 4 + 6 + 7 + 3) + 9) + 9
8 * ((4 + 7 * 4) * 6 + 3)
((2 + 2 + 5 * 9) * 9 + 2 * 8 * 8 * 3) * 7
(8 + 9 * 2 + 2 * 3 * 6) + (4 * 7 * (2 * 2) + 9 + 7) * 2 + 7 * 9 * (8 * 7 * 2 * 4)
(7 * (2 * 4 * 3 + 5 * 4 + 5)) * 3 * 7 * 9
2 * 6 + 9 + 5 + ((9 * 2 * 5 + 7) * 6) + 8
(8 * (6 * 4 * 5 * 5 + 5 * 2) * 7 + 7 * 6) + ((4 * 5 * 4) * 4)
(8 * 8 * (2 + 3)) * 2 + 8 + 5 * ((9 * 5 + 3 * 2 + 5 * 2) * (3 + 5))
7 + 8 * 4 * ((4 * 6 + 2 * 2 * 7) * (6 + 9) + 4) + 2 + 6
3 * 5 * (2 * 5 * 9 + (5 * 8 * 8))
(4 + 2) * 4 * 5 + 8 * ((2 + 8 * 5 + 7) * 9 + 9) * (6 + 3 * 3)
((9 + 8 + 8 + 4) * 6) * 5
2 + (2 * 9)
(4 + 2) + ((8 * 9 * 3 + 2 * 5) + (2 * 3 * 9 * 6 + 8 * 9) * 9 * 4 * 6) + 8 + 8 * ((3 * 9) * 8 + 9 + 6 * 5 + 3)
(5 * 8 + 5 * 2 + 3 * 5) * (8 + 7) * 2 * (2 + 5) * 7 * 7
7 * 5 * 4 * 4
((2 * 9 + 9 * 9 + 8) + 6 + 7 * 7 + 2 + 4) * 4 + 2
(8 * 2 + 9 * 7 * (2 * 4 * 6 * 7 + 7 * 8)) + 2 * 7 * 9 + 2
3 + 3 * 9 * 6 + 9
(6 + (6 * 7 + 4 * 7) + 5) + 8 + 3
7 * 7 + (9 + (5 + 4 * 3)) * 2 * (4 * 4 + 3 * 4)
4 * 9 + (3 + (6 * 6 * 9 + 8 + 4) + 4 + 7 + 6)
8 + 4 * ((9 * 2 * 2 + 8) + 7 * 7) + 8 + 9
9 + 6 * 6 * (3 + (2 * 5) + 9 * 3 * 7) + 6
9 + (5 * 6 * 7 * 4 + 8 * 9) + 7
9 + 7 * (3 + 8 + 2 + 4 + 5 * 3) + 8 + (5 * (4 * 5 * 5 + 2) * 6 * (7 + 4 * 7 * 2 * 5 + 2)) * 7
(3 * 2 * 6 + 7) + 7
9 * 8 * 4 + 9 + 4 * (5 * 5 * 6 * (3 * 3 + 9) * 9 * 7)
(8 * 4 * 9 * 9 + 4 * 4) + 7 + 7
(3 + 3 + 2 * 4) + 4 * 5 * (7 + 4 * 3 * 9 + 4) * 3
7 + (2 + 3 * 4 + 2 + (9 + 7) * 5) + 5 * 3 * 9
7 + ((9 * 8 * 2 * 3 + 7) * 5 + 5 + 4 * 5) + 3 * 8 * 4 + 4
4 * ((8 + 3) + 8 + 5 + (6 + 2 + 9 + 2 + 7) + 8) + (8 * 9 * 8)
9 * (5 + 5 * 8 + 8) + 2 + 7 * 7
3 + (5 + (8 * 5 * 3 + 9 + 8 * 7)) * ((7 * 5) * 5 * 4 * 2) + 9
2 + 4 + (7 * 8 + 8 + 5 * 8) + (6 + (2 + 7 + 9 + 6 * 9) * (6 + 7 * 5))
2 + 8 + 7 + ((5 * 5) * 6)
2 * (9 + (6 + 6 * 6 * 9) + (3 + 5 + 6 * 8 + 7 * 5))
(3 + 8 + 3 * 3 * 3) * 7 * (2 * (8 + 4 + 4 * 8 * 7) * 7 * 4) + ((8 + 2 * 4) * 4 + 7 + 6 + 4 + 2)
6 + 5 + 9 * (8 * (7 * 5 * 6 * 3 * 7 + 3)) * 3 * 3
5 + ((3 * 7 * 7 + 5 + 2) * (6 * 4 + 4 + 6 * 9) + 3 * (5 + 6 * 4 + 6 * 6 + 4) + 9)
(2 + (5 + 5 + 4)) + 6
6 + 8 * (8 + 7 + 4 + 2 * 3)
(7 * 9 + 4 * 2) + 4 * 9
2 + (3 * (7 * 6 + 4 * 2 * 6) * (3 + 6 + 4 * 9 * 9 + 3))
7 + 4 + 2 + (6 + 8 * (9 + 2 + 9 * 6) * 7 * 8 * 9)
9 + (8 + 2 + (7 + 9 + 5 * 8 + 3 + 4) * 8 + 2) + 7 * (4 * (7 * 3 + 7 + 2 + 9 * 5) + 3 + 4 + 3)
5 * (3 + 3 + 8 * 7) * (8 + (3 * 3) + 8) + 8 * (7 + 5 + (8 * 3 + 2) * 9 + 8)
(4 + 6 + 2 + (7 + 4 * 9) * 8) + 8 + 8
(3 + (8 * 5 + 6 + 4 + 6 * 3) + 5 + 8 * 5) + 3 + 8 + 8 + 3 + ((4 * 5 * 5 * 6) * 9 * 3 + 4 + 2 + 6)
2 * 8 * 4 + (8 * 2 + 7 * 2 * (9 * 9 + 8 + 4 * 3 * 4) * 6) + 5
((4 + 7 + 2) + 9) + 6 + 8 * 9 * 7 + 3
(2 + 9) + 3 * 4 * 6
7 * 4 * ((2 * 8 * 7) * 8 * 7) + 3
2 + 8 + 7 * (5 * 9) * 7 + 5
7 + 2 + 3 + 5 * (6 * 8 + 7 + (7 + 5 * 9 + 5 + 5 + 3)) * 9
6 + 3 * (5 + 4 * 9 + 9 + 9 + (5 * 9 * 3 + 2 * 5 * 6)) * 6 * 7 * 3
2 * 7 + 5 + 3 + 2 + 5
6 * 4 + (5 * 3) + 6 + (6 * 9 + 9 + 7 * 4)
(3 * 9 + 6 + 4 * (3 * 6 + 8 * 4) * 7) + 8
3 * (3 + 7) * 3 + 4 + 6 * 4
8 + (2 + (7 + 4 * 5 + 9 + 2)) * 7 + 2
2 + (4 + 9 * 5 + (2 * 3 + 5 * 2 * 7 * 8) * 4) * 5
8 + ((8 + 6 * 9 * 8 * 5 * 7) * 4 * 2 * 6)
(5 * 9) * 8 * (5 + 9 * 3 + 4 + (9 + 2 * 6 * 3 + 8 * 8) + 5) * 6
((3 + 6 * 5 * 2) * 7 * 2 * 6 + 6) + 7 + 7 + 2
8 + 8 + 7 * 2 * 3
5 * ((4 + 2 + 4 * 7) + 5 + 2 * 9) * 6
2 + 5
(6 + (6 * 4 + 6) * 8 * 9 + 4 * 3) + 8 + 9 + (6 + 3 * 4 + 2 + 6) * (3 * 4)
(6 * 9 * 8 * 9 * 7 + 6) + 6
3 * (4 * 2 + 8 + (6 * 5 * 3 + 4) * 4) * 5 * 3
9 * (4 + 2 + 5)
2 + 9 + (5 + (7 + 9) + 4 * 6 * 3)
((4 + 2) + 7) + 6 * 7
(8 * 9 + 6 * (4 * 2)) + 5
8 * (9 * (6 + 8 * 8 * 8 + 7 * 8) + 4 + 6 + 9 * (8 + 3 * 7 * 6 * 2))
2 + (4 + (9 + 5)) + 8 * 6 * 5
2 + (2 + (3 + 8 * 9 * 8 * 2) * 6) + 2 + (4 * 2 + 3 * 9)
((3 + 3) + 9 + 7 * 8 + 9) + (8 + 7 * 6) + 8 + 8 + (4 * 2 * 3 + 8 + 9)
((9 + 6 + 2 * 6 * 8 + 6) * 8) + (8 + 7)
9 * 6 * 3 + (9 * 5 + (7 * 2 * 9 * 9 * 9 + 3) + (4 + 4))
3 + 5 * 9 * 5 * 5 * 5
3 + (4 + 6) + (4 * (4 * 5 * 2 + 9 + 8 + 4) + 3)
(4 * 4) + (4 * 2 + 4 * 2) + 7
((5 * 3 * 8) + 6 * 4 * 5) + 5 * 2 * 6
2 + 7 * 5 * (2 * 9 * 9 + (4 * 5 * 5 * 6 + 6 * 4) * 6) + 2 * 7
6 * 7 + 9 + (7 * 7 * 7 * 2 * 3 + (7 * 9 + 9 * 9)) * 8 + 3
(5 * 6 + (7 + 6 + 3 + 2 * 6 + 3)) + (2 * (3 + 4 * 6)) * 7 * 5 + 6 * ((2 * 2 * 5) + (2 * 5 + 9 + 3 * 9) * (5 + 7 + 7 + 4 * 9 * 5) + (8 + 5 + 8 * 7 + 2))
5 + 2 * (5 + (8 + 9 * 2 * 6 + 5 * 8) + 4 + 8 * (4 + 4) * 7)
(6 * 9) * 2 * (5 * 8 * 8) + 8
(3 + 8 * 7) * 3 * 5 * 7 * 7
((7 + 4 + 5 + 9 * 4) + 6 + 5 * (2 + 7 * 8 * 2 * 7 * 2)) + 8
7 + ((3 * 6 + 7 + 8 * 5 + 6) * 5 + (7 + 2 + 7 * 6 * 8 * 7) + (6 * 5 * 8 + 8) + 6 * 9) + 3 * 4 * 3 * 8
2 + 9 * ((7 + 6) + (5 * 8 * 9 + 6) * 7 + 5 + 9) * 9
(6 + 3 * 5) + 5 + 9 + (7 + 9 * 5 * 7) + 6 * 5
6 * 2 * 6
(5 * 5 + (2 + 7 * 8 + 6 * 6) * (3 + 3 * 2 + 5 * 8 * 7) * 2 + 4) + 4
5 * 8 + 7 + (8 * 4 + 8) + 5 * 9
2 + 7 + ((4 * 2) * 5 * (5 + 7 * 7 * 4 * 8 * 9)) + 3 + 6
4 * ((2 * 5 + 9 * 9) * 2 + 6 * 9) + 7 * ((8 * 4 * 7 + 9 * 9 * 4) * (7 * 4 + 8))
3 + 6 + 2 * 5 * ((5 + 6 * 8 + 7 + 3 + 3) * 2 + (4 + 2 + 6 + 4 + 6 + 3) * 6 * 2) * (6 + 6)
6 * 9 + 4 * 2 + (9 * 4) + 6
7 + ((2 + 3 * 9 * 4 * 5) + 6 + 8) + 2 * 7
5 * 7 * 8 + 2 * (9 * 4 + (5 * 7)) + 8
(4 + 4 + 5 + (6 * 9 * 9 + 9 + 2 * 7) * 4) + 9 * 8
((8 + 2 + 4 + 6) * 4 * 2 + 6 + (9 + 9) * 7) + 4 * (5 * 5)
4 * 9 + (3 * (5 + 5 * 8 + 8) + 3 * 6 * 3) + 5 * 3 * 4
2 * 9 + (9 + 6 + 2 * (3 + 9 * 8 * 7 * 6 * 6))
(2 + (2 * 9 + 4) + (5 + 8 + 2 * 3) * (8 + 2 * 8 + 8 * 8 * 2)) + (5 + 3 * 5 * (6 + 3)) + 8 * 3
8 + (6 + 3 * 2 * 9 + (3 * 6) * 6) + 8 * (9 + 8) + 2 + 7
(4 * 5 + (2 + 2 + 5 * 7 * 9) + 2) * 3 * 3 + 8 * 7 * 7
(8 + 3) * (4 * 3 + 7 + 4) + (4 + 7 * 2 + 2) * 4 + 6
2 * 6 * ((2 * 2 * 9 + 6 + 9 + 5) + (6 + 2)) + 3 * 2 * 9
4 * 5 * (8 * 7) + (8 * 5 * 8 + 3 + (2 + 8 * 8 + 3) * 3)
3 + 4 + 7 + (6 * 3) + ((5 + 5) + 7 + (3 * 2 + 7 + 2 + 7 * 6) + 3 * 6 + (4 + 9 * 3 * 5 * 2)) * 9
9 + 5 * 6 + (6 + (3 + 9 * 9 * 7) + 6 * 4 + 9 + 8) + 8 + 5
6 + 4 + 2
4 + 8 + 6 * (8 + 7 * 3 * 7 * 7 * 2) + (7 + 4 * 9) * ((7 * 8) + 7 * 6 + 9 * 5 * (4 * 4 * 5 * 8))
3 + 3 + (4 * 6 * 9 * 5 + 9) + (3 + 4 + 2 * (6 + 3 * 3 * 9 * 3))
9 * 6
(4 * 9 * 4 + 8 * 4) + 3 * 7 + 5
9 + (2 + 4 * 4 + 7 * (6 * 6 * 9)) + 2 * 6
((2 + 8 + 9 * 8) + 9 + 3) + 4 * 3 + 2 + 6
3 * 7 * 5 * (2 * (2 * 7 * 9) + 9) + 8
6 + 7 * 7 + (5 + 3 + 4 + (4 * 9 * 8 + 2 * 5) + 7) * 6 * 9
2 * ((5 + 5 * 3 * 3 * 8) + 3 * 4) * 9 * 9 * 8
(2 * 7) + 9 * 5 + 9 + 4 * (8 * 5 * (8 + 6 * 8 + 8 + 2) * (2 + 7) * (6 + 7 * 6 + 4 * 2 + 2) + 8)
5 * 7 + 7 + 3
2 + 3 * (5 + 8 + 6 * 9 * 5) + 9 * 6 + 7
(7 * 5 + 5 * 7 + 3 + 3) * 6 + (5 + 6 + 3)
9 * 7 + (9 + 5 * 9 + 7) + 9 * 5 + 5
(7 * (6 * 7 + 3 * 3 + 2 * 6) + (6 * 6) + 6 + 7 + 9) * 4 * 9 + 3 * 8 * 5
7 + 7 * 7 + (3 + 9 + 4 + 5)
(8 + (6 * 7 * 6 * 9 + 8 * 7) + 4 * 2 + 4 + (4 + 5 * 8 + 5 * 9 + 5)) * (2 + 9) * 8 * 5 * 4 * 6
(9 * (6 + 8 + 5) * 6 * 6) + 3
2 * (4 + 3 * 5 + 3) + (9 * 3 + 2 + 3) + 2 * 2
4 * (2 * 5 * 3 + 4 * 3 + 5) + 9 * (4 + 7 + 2 * 4)
9 + 5 * 8 + 5 + 4 * (2 * 8 + 8)
9 + (7 * 3 * 6 + (9 * 7 * 8 + 2 * 3 + 4)) + 4
6 * 3 * (8 * (3 * 8 * 5 * 8 + 6) * 3) * 6 * 4
5 + 7 + ((4 * 4 + 4) * 5 * 2 * 2 + 7 + (5 + 5 * 4 + 8 + 3 * 5)) * 9 + 9
((4 * 8) + 6 * 8 * (3 + 3 + 2 * 3 + 7 * 7)) + 7 + (3 * 2)
4 + (7 + 6) + 7 + 7 + (5 + 2 + (5 * 8 * 4) + 7 * (5 * 7) + 2) * 5
(7 + 7 * 8 * 7 + 2 * 6) + 6 * 4 + 2 + 2
(7 + 7) + 8 + 5 + 2 * 5 * 3
((2 * 9 * 8 + 5) * 3 + (4 + 3 + 6 * 9)) * 3 * (9 + 3)
5 * (3 + (4 * 6 * 5 * 9 + 9) * 8) * 8 * 5 * 4 + 5
2 + 3 * 2 + 7 + (5 + 8 + 2)
7 * (6 + (6 + 2 + 8 + 8 + 8)) + 6 + 4 * 8
(8 * 8 + 3 * 2 * 2) + 7
(7 * (8 + 3 + 8) + (2 + 4) * 8 + 2 * 8) * 4 + 3 * 9
8 + (3 * (7 * 6) + (5 * 6 * 5) + 8 * 5) + 7 + 8 * 3 + 5
7 * (4 + 2 * 5 * 8) * 2 * 5
6 * (5 + 3) + 7 * 2
3 + 4
7 + 7 * 6 * ((5 + 3 + 3 * 8) + 4 + 8 * 7 * 9) + 8 * 3
6 + 4 * 6 + 6 * (3 * 4 + 5 * 3 * (8 * 8 * 8 * 5 + 8) + 5)
7 + (5 + 7 + 7 * (2 * 3 * 2 * 6 * 7 + 9)) * 6 + 5 * 2
2 + (4 * 8 + 6) * 2 * 4 + 7 + 2
(5 + 4 + (6 + 6 * 2 * 8) + 8 * 3) * 9 * 8 * 2 * 6
2 * (7 * 6 + 7 * 3 + 6 + 6) * ((8 + 8 + 5) * (9 * 4 + 4 + 3 * 3) * 8 + 2 + 5) * 2 * 4 * 9
3 + (5 * 9 + 3 * 4 * (6 + 4 + 7 * 7 * 5 * 7)) * 3 * (7 * (6 * 2 * 9 * 7 * 4 + 3) + 8 * 7 + 4) + (5 + 3 + 6 + 9 * 8)
7 + (4 * 8 * 9 * 6 * 5 + 6) + (6 + 5 + 2 * 5) + 7 * 4 + 5
(9 + 4 + 6) + 9 + 8 + (7 + 9 + 7 + (2 + 5 + 5 + 8 * 4) * 2) * 4 + (5 + (3 * 7 + 6))
(3 + (5 + 4 * 8) * 6) * 9 * 2 * 3 * 4 * 8
8 + (6 * 4 * 3 + 3 + 7) + ((4 * 4 + 9 * 8 * 6 * 8) + 9 * 7 + 2) + 9
4 + 3 + ((7 * 7) + 9 * 9 + (3 + 5 * 8))
3 + 8 + 4
(2 * 5 + 2 + (9 + 6 * 3 * 9 + 3)) * ((4 + 6 * 6) * 8 + 2 + 5) + 8
9 * (6 + 2 * 6 * (6 + 5 * 9) * 2 * 5)
5 + 4 * (4 + (6 + 9 + 8 + 5) * 2 + 9 * (8 + 2 * 2 * 5 * 3)) + (6 + (3 + 8 * 7 * 6 * 5 * 6) * 9) + 6 * 3
(3 * 6) * (8 + 2 * 6) * (5 * 5 + (9 * 8 + 9 * 4) * (3 * 3))
8 + (6 + 5 * (7 + 9 + 5 + 5 + 6 * 4) + 5 * 2 + 9) * 3 + 2 + 7 * 5
(6 + 5) + 7 * 7
(4 + 7 + 3 + 5 + 5) * 3 + 7
(5 * 3 * 4) + 9 + 2 + 5
(4 * 6 * 6) * 7 + 4 + ((3 * 4 * 5) * (5 + 5 + 9 * 7) + 7 + 9 + 9 + 7) * 5 + 8
7 * 4 + 8
((4 + 8 + 8 + 2 + 4) + 6) + 7 * 4
(8 * 8 + 3) + (4 + 3)
2 + (8 + 8 + 3 + 3 + 3)
2 * ((7 + 2 * 8 + 2) * 8 * 3 * 2) * 8 + 8 * 3 + 3
8 * 7 + (9 * 2 * 3) * 4
5 + (7 * 8 + 2 * 8 + 8) * 9
((3 + 9 + 4 + 3) + 9 + (3 + 8) * (8 + 7 * 7 + 3 * 6 * 3) * (8 + 7) * 3) + 8 + 5
8 * 9 + 8 * (4 + 6 * 8 * (6 + 4 + 4 * 8) * 5 * 6) + 4
(4 * 8 + 8 * (5 + 4) * 9 + 3) * 9
8 * (4 * 2 * 7 + 5 + (5 + 5 * 5 + 7 * 4 + 7))
2 + (3 + 9 * (4 * 2)) + 5 * 3 * 4 + 5
6 * 2 + ((8 * 9 * 4 * 8 * 6) * 7 + 3 * 9)
2 + (9 + (8 + 4 * 8 + 5 * 4) * 6 * 7 + (5 + 3 + 9 * 2 * 4 * 2) * 5) * 9 * 2
6 + 2 + 3 + 8 * (8 * 5 * 3 + 8) * (5 + 2 + 5)
4 * (6 * 8 + (5 * 6) + 2) * 9 * 8 + (3 + 2 + 4)
9 * 5 * 3 + (4 * 6 + (3 * 7 + 6 + 5 + 8))
(4 + 5 * 5) + 2 * 4 * 9 + 2 + (7 * 9 * 3 + 4 * 5 * 6)
7 + 9 * 6 * (6 + 8 + 3 * 6 + 4 + 6)
(9 * 3 + 5) + 7 * 4 + (3 * 8 + 6 + (8 * 4) * 4 + (4 + 4 * 6 * 4)) * 3
9 * 6 * 7 * (4 * 4 + (2 * 6 * 6 * 4 * 8 + 3) * 7 * 2 * 8) * 4 * 8
3 * 9 * (8 * 2 + 2 * (3 + 6) * (5 + 9 + 6)) + (5 * 4)
9 * 4 + 6 * ((4 + 2 + 9 * 2) + 3 * 9 + 4) + 6
4 + (4 + (3 + 9 * 5 + 7) + 4 * 7)
(2 + 9 * 3 * 6 + 7) * ((2 + 6 * 6 * 5 * 8 * 7) * 8 * 4 + 2)
(4 * 2 * (4 * 7 + 4 * 2) * 5 * 2 * (6 + 6 + 9 * 8)) + 4 * (9 * 9 + 7 * (8 * 4 + 5) * 4) + 4
3 + (6 * (3 + 8 + 3 + 9 * 5) + 3 + (4 + 9 + 3 + 4 * 3 + 4) + 6)
(9 + (5 * 6 + 2 * 7 * 4) + 3 + 3 + 9 + 4) * 5 + 9
4 * ((9 * 7 * 4) + 9 * 4 * 3) * (6 + 6 + 3 + 4) * 3 * 5
4 + 2 + (4 + 2 * 2 * 4 * 7 + 6) * 3 * (5 + 6 + 6 * (4 * 6 + 2) * 3)
(9 * 8 * 9 + 3) + 4 + (8 + (7 + 3 * 9)) + (7 + 5 + (7 * 2 * 5 + 6 * 8 * 5)) * (7 + 3 * 9 * 9 + 4 * 7) + 4
3 * 6 + 4 + 6 * 3
8 * 3 + (3 * 6 + 5) + 9 + (9 + (7 + 6 * 9 * 2 * 8) + 8 + (5 + 7 * 3 + 8 + 4 + 3)) * 9
6 * 7 + (6 * 9 * 9) * ((9 * 2) + 6 * 7 + 3 * 5)
(3 * 7) + 2 * 3 + 4 + (5 * 8 + 7 + 9 * 7 * 7)
6 * 2 + 3 * 6 + (6 * 7 * 2 * 4) * 8
4 + ((2 + 7 * 2 + 6 * 2) * (6 * 4 + 3) * 9 * 2 + 4 + 8) * 5 * 3 * 2 + 2
9 + (4 + 5 * 9) * 2 * (5 + 8 * 8 + 2 + 2 * 2) * 4 * (3 * 3 + 3)
3 * 7 * 7 + (8 + 7 * 5 * 7) * 9 + (4 * 2)
(9 * 6 * 6) + 4 + 9 * 2 + 4 + 3
9 * 7 + 6 * 8
(7 + 5 * 5 * 2) + 2 + 7 + 8 * 8
2 * 7 * (6 + 2) + 2 + 2 * ((8 * 5 + 2 + 8 + 9 * 6) + (4 * 8) + 8 + 9 + (4 + 8 * 9 * 7 + 2))
4 + 8 * 2 * 9 + (9 + 3 * 3 + 4 * 5) * 2
5 + (6 * (9 + 3 * 9 + 7 + 9 * 2))
9 * 7 * 9 + (5 * (6 * 8 + 5 + 3) + (2 * 3 * 5))
((2 * 5 * 3) + 6 * 4 + (5 + 3 + 2 * 9)) + (5 * 9) + 9
((3 + 2) + (6 * 3 * 4) + 5) * 5 * 8 * (9 * 9 + (6 + 9 + 4 * 7) + (2 * 9 * 8 + 4 * 8 + 3) + (5 + 5 * 7)) + 2 + 8
7 + 4 * 2 * 3
((3 + 3) * (2 + 6 * 3 * 8) * 7 + 8) + 2 + ((4 + 6 + 3) * 7 * 9 + 9) * 4 * 7 * (6 * (6 + 3 + 4 * 3) + 4)
9 + (9 + 7 + 3) * 6 + (2 + 9)
5 + ((3 * 3 + 4) + (9 + 8) * 9) + 2 + 9
9 * 3
8 + 4 + 5 + (9 + 6 * (9 * 7 * 4 * 9) * 3) + 7
((9 + 9 * 8 + 4 + 6) + (6 * 7 + 4 + 2 * 2 * 3) * 6 * 8) * 3 + 2 + 7 + 3
4 + 4 * 6 + ((8 * 8 * 2) * (3 * 5 + 7 + 2 * 6 * 2) * 4) * 8 * 9
(6 + 4) + (8 + 9 * 9 + 5 + 4 * 8) * 4
3 + 2 + 5 * (5 * 9 * 5 + 4 * 6)
2 + 6 * 8 + (5 + 3 * 6 + (7 + 6 + 3 + 3 * 7))
3 * (7 * 9 + 4 + (4 + 4 + 3 + 4 + 3) + (4 * 6 + 2 * 6)) + 6 + 7 + 6
9 + 5 + 2 * (7 + 7 + (4 + 3 * 8 * 5) * 2) + 6 * 7
(2 + 5 + (9 * 9 * 3 + 6 + 3 + 3)) * (8 * 7 + 4 * 8 * 6)
(4 + (5 + 6 + 5 + 3 * 9 + 9) * 2 * (4 * 5) + 4) + 6 * 2 + 7
9 + ((3 * 8 + 7 * 3) * 7 + (3 * 6 + 5)) + (9 + 9 + 9 * 8)
(7 * 6 + 7) * 5 + 8
3 * (8 + (9 + 9 + 4 * 3 * 6) + 7)
"""

import tokenize
import io

class Number:
    def __init__(self, n):
        self.n = n

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__mul__(Number(other))
        elif isinstance(other, Number):
            return Number(self.n * other.n)
        return NotImplemented
    __rmul__ = __mul__

    # @ has the same precedence as *, so use it to represent +
    def __matmul__(self, other):
        if isinstance(other, int):
            return self.__matmul__(Number(other))
        elif isinstance(other, Number):
            return Number(self.n + other.n)
        return NotImplemented
    __rmatmul__ = __matmul__

    # - has the same precedence as +, so use it for the lower precedence *
    def __sub__(self, other):
        if isinstance(other, int):
            return self.__sub__(Number(other))
        elif isinstance(other, Number):
            return Number(self.n * other.n)
        return NotImplemented
    __rsub__ = __sub__

    def __str__(self):
        return f"Number({self.n})"
    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other, int):
            return self.n == other
        elif isinstance(other, Number):
            return self.n == other.n
        return NotImplemented

def evaluate(expr, part=1):
    new_tokens = []
    for tok in tokenize.generate_tokens(io.StringIO(expr).readline):
        t = tok.exact_type
        s = tok.string
        if t == tokenize.NUMBER:
            new_tokens.extend([
                (tokenize.NAME, "Number"),
                (tokenize.LPAR, '('),
                (t, s),
                (tokenize.RPAR, ')'),
            ])
        elif t == tokenize.PLUS:
            new_tokens.append((tokenize.AT, '@'))
        elif part == 2 and t == tokenize.STAR:
            new_tokens.append((tokenize.MINUS, '-'))
        else:
            new_tokens.append((t, s))

    expr = tokenize.untokenize(new_tokens)
    return eval('Number(0) @ ' + expr)

print("Day 18")
print("Part 1")
print("Test input")
for expr, result in test_inputs.items():
    ans = evaluate(expr)
    if ans == result:
        print(expr, "OK")
    else:
        raise RuntimeError(f"{expr} gave {ans} instead of {result}")
print("Puzzlie input")
S = 0
for line in input.strip().splitlines():
    S @= evaluate(line)
print(S)

print("Part 2")
print("Test input")
for expr, result in test_inputs2.items():
    ans = evaluate(expr, part=2)
    if ans == result:
        print(expr, "OK")
    else:
        raise RuntimeError(f"{expr} gave {ans} instead of {result}")
print("Puzzlie input")
S = 0
for line in input.strip().splitlines():
    S @= evaluate(line, part=2)
print(S)
