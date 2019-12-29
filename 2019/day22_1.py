from sympy import mod_inverse

import numpy as np

import re

def parse_input(I, N):
    a = np.arange(N)
    b = a.copy()
    for line in I.strip().splitlines():
        m = re.match(r'deal with increment (.*)', line)
        if m:
            b = b[int(mod_inverse(int(m.group(1)), N))*a % N]
            assert len(np.unique(b)) == N, line
            continue
        m = re.match(r'deal into new stack', line)
        if m:
            b = b[::-1]
            assert len(np.unique(b)) == N, line
            continue
        m = re.match(r'cut (.*)', line)
        if m:
            b = b[(a + int(m.group(1))) % N]
            assert len(np.unique(b)) == N, line
            continue
        raise ValueError("Unrecognized input: %s" % line)
    return b

test_input_1 = """
deal with increment 7
deal into new stack
deal into new stack
"""

test_input_2 = """
cut 6
deal with increment 7
deal into new stack
"""

test_input_3 = """
deal with increment 7
deal with increment 9
cut -2
"""

test_input_4 = """
deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1
"""

with open('day22-input') as f:
    input = f.read()

def main():
    print("Day 22, test input 1")
    res = parse_input(test_input_1, 10)
    print("Should be 0 3 6 9 2 5 8 1 4 7")
    print(res)
    print()

    print("Day 22, test input 2")
    res = parse_input(test_input_2, 10)
    print("Should be 3 0 7 4 1 8 5 2 9 6")
    print(res)
    print()

    print("Day 22, test input 3")
    res = parse_input(test_input_3, 10)
    print("Should be 6 3 0 7 4 1 8 5 2 9")
    print(res)
    print()

    print("Day 22, test input 4")
    res = parse_input(test_input_4, 10)
    print("Should be 9 2 5 8 1 4 7 0 3 6")
    print(res)
    print()

    print("Day 22, part 1")
    res = parse_input(input, 10007)
    print(res)
    print(np.where(res == 2019)[0][0])

if __name__ == '__main__':
    main()
