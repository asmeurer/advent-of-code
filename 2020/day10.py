test_input1 = """
16
10
15
5
1
11
7
19
6
12
4
"""

test_input2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

input = """
8
40
45
93
147
64
90
125
149
145
111
126
9
146
38
97
103
6
122
34
18
35
96
86
116
29
59
118
102
26
66
17
74
94
5
114
128
1
75
47
141
58
65
100
63
12
53
25
106
136
15
82
22
117
2
80
79
139
7
81
129
19
52
87
115
132
140
88
109
62
73
46
24
69
101
110
16
95
148
76
135
142
89
50
72
41
39
42
56
51
57
127
83
121
33
32
23
"""

import numpy as np

def get_array(text):
    l = sorted(map(int, text.strip().splitlines()))
    return np.array([0] + l + [l[-1] + 3])

def count1(a):
    d = np.diff(a)
    ones = np.sum([d==1])
    threes = np.sum([d==3])
    return (ones, threes)

print("Day 10")
print("Part 1")
print("Test input 1")
test_a1 = get_array(test_input1)
print(test_a1)
print(np.diff(test_a1))
ones, threes = count1(test_a1)
print(ones, threes)

test_a2 = get_array(test_input2)
print(test_a2)
print(np.diff(test_a2))
ones, threes = count1(test_a2)
print(ones, threes)

print("Puzzle input")
a = get_array(input)
ones, threes = count1(a)
print(ones, threes)
print(ones*threes)
