test_input = "3,4,3,1,2"

input = "1,4,1,1,1,1,5,1,1,5,1,4,2,5,1,2,3,1,1,1,1,5,4,2,1,1,3,1,1,1,1,1,1,1,2,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,4,1,1,1,1,4,1,1,5,5,1,1,1,4,1,1,1,1,1,3,2,1,1,1,1,1,2,3,1,1,2,1,1,1,3,1,1,1,2,1,2,1,1,2,1,1,3,1,1,1,3,3,5,1,4,1,1,5,1,1,4,1,5,3,3,5,1,1,1,4,1,1,1,1,1,1,5,5,1,1,4,1,2,1,1,1,1,2,2,2,1,1,2,2,4,1,1,1,1,3,1,2,3,4,1,1,1,4,4,1,1,1,1,1,1,1,4,2,5,2,1,1,4,1,1,5,1,1,5,1,5,5,1,3,5,1,1,5,1,1,2,2,1,1,1,1,1,1,1,4,3,1,1,4,1,4,1,1,1,1,4,1,4,4,4,3,1,1,3,2,1,1,1,1,1,1,1,4,1,3,1,1,1,1,1,1,1,5,2,4,2,1,4,4,1,5,1,1,3,1,3,1,1,1,1,1,4,2,3,2,1,1,2,1,5,2,1,1,4,1,4,1,1,1,4,4,1,1,1,1,1,1,4,1,1,1,2,1,1,2"

import numpy as np

def parse_input(data):
    a = np.zeros(9, dtype=int)
    d = map(int, data.split(','))
    for i in d:
        a[i] += 1

    return a

def increment_ndays(a, n):
    for i in range(n):
        A = np.roll(a, -1)
        A[6] += a[0]
        a = A

    return a

print("Day 6")
print("Part 1")
print("Test input")
test_a = parse_input(test_input)
print(test_a)
for i in range(1, 6):
    print("day", i, increment_ndays(test_a, i))
print("total after 18 days", increment_ndays(test_a, 18).sum())
print("total after 80 days", increment_ndays(test_a, 80).sum())

print("Puzzle input")
a = parse_input(input)
print(a)
for i in range(1, 6):
    print("day", i, increment_ndays(a, i))
print("total after 18 days", increment_ndays(a, 18).sum())
print("total after 80 days", increment_ndays(a, 80).sum())

print("Part 2")
print("Test input")
print("total after 265 days", increment_ndays(test_a, 256).sum())

print("Puzzle input")
print("total after 265 days", increment_ndays(a, 256).sum())
