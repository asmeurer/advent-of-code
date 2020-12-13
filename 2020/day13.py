test_input = """
939
7,13,x,x,59,x,31,19
"""

input = """
1000052
23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,863,x,x,x,x,x,x,x,x,x,x,x,19,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,571,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41
"""

import numpy as np

def parse_input(text):
    now, times = text.strip().splitlines()
    now = int(now)
    times = np.array([int(i) for i in times.split(',') if i != 'x'])
    return now, times

def first_time(now, times):
    waits = times - (now % times)
    return np.min(waits), times[np.argmin(waits)]

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
