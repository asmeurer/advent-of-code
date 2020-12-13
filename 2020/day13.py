test_input = """
939
7,13,x,x,59,x,31,19
"""

test_input2 = "17,x,13,19"
test_input3 = "67,7,59,61"
test_input4 = "67,x,7,59,61"
test_input5 = "67,7,x,59,61"
test_input6 = "1789,37,47,1889"

input = """
1000052
23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,863,x,x,x,x,x,x,x,x,x,x,x,19,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,571,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41
"""

import numpy as np
from sympy.ntheory.modular import crt

def parse_input(text):
    now, times = text.strip().splitlines()
    now = int(now)
    times, locs = parse_times(times)
    return now, times

def parse_times(text):
    times = np.array([int(i) for i in text.split(',') if i != 'x'])
    locs = [i for i, x in enumerate(text.split(',')) if x != 'x']
    return times, locs

def first_time(now, times):
    waits = times - (now % times)
    return np.min(waits), times[np.argmin(waits)]

def solve_time_orders(times, locs):
    res, l = crt(times, locs, symmetric=True)
    if res > 0:
        res -= l
    return abs(int(res))

print("Day 13")
print("Part 1")
print("Test input")
test_now, test_times = parse_input(test_input)
print(test_now, test_times)
test_wait, test_id = first_time(test_now, test_times)
print(test_wait, test_id)
print(test_wait*test_id)

print("Puzzle input")
now, times = parse_input(input)
print(now, times)
wait, id = first_time(now, times)
print(wait, id)
print(wait*id)

print("Part 2")
print("Test input")
times1, locs1 = parse_times(test_input.strip().splitlines()[1])
print(times1, locs1)
print(solve_time_orders(times1, locs1))

times2, locs2 = parse_times(test_input2)
print(times2, locs2)
print(solve_time_orders(times2, locs2))

times3, locs3 = parse_times(test_input3)
print(times3, locs3)
print(solve_time_orders(times3, locs3))

times4, locs4 = parse_times(test_input4)
print(times4, locs4)
print(solve_time_orders(times4, locs4))

times5, locs5 = parse_times(test_input5)
print(times5, locs5)
print(solve_time_orders(times5, locs5))

times6, locs6 = parse_times(test_input6)
print(times6, locs6)
print(solve_time_orders(times6, locs6))

print("Puzzle input")
times, locs = parse_times(input.strip().splitlines()[1])
print(times, locs)
print(solve_time_orders(times, locs))
