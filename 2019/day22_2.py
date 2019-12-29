from sympy import symbols, lambdify

import numpy as np

import re

def parse_input(I, N):
    expr = symbols('x')

    for line in I.strip().splitlines():
        m = re.match(r'deal with increment (.*)', line)
        if m:
            expr = expr*int(m.group(1))
            continue
        m = re.match(r'deal into new stack', line)
        if m:
            expr = -expr - 1
            continue
        m = re.match(r'cut (.*)', line)
        if m:
            expr = expr - int(m.group(1))
            continue
        raise ValueError("Unrecognized input: %s" % line)
    return expr % N

test_input_1 = """
deal with increment 7
deal into new stack
deal into new stack
"""

test_answer_1 = np.array([int(i) for i in '0 3 6 9 2 5 8 1 4 7'.split()])

test_input_2 = """
cut 6
deal with increment 7
deal into new stack
"""

test_answer_2 = np.array([int(i) for i in '3 0 7 4 1 8 5 2 9 6'.split()])

test_input_3 = """
deal with increment 7
deal with increment 9
cut -2
"""

test_answer_3 = np.array([int(i) for i in '6 3 0 7 4 1 8 5 2 9'.split()])

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
    x = symbols('x')

    print("Day 22, test input 1")
    expr = parse_input(test_input_1, 10)
    print(expr)
    print(lambdify(x, expr)(test_answer_1))
    print(lambdify(x, expr)(2))
    print()

    print("Day 22, test input 2")
    expr = parse_input(test_input_2, 10)
    print(expr)
    print(lambdify(x, expr)(test_answer_2))
    print()

    print("Day 22, test input 3")
    expr = parse_input(test_input_3, 10)
    print(expr)
    print(lambdify(x, expr)(test_answer_3))
    print()

    print("Day 22, part 1")
    expr = parse_input(input, 10007)
    print(expr)
    print(lambdify(x, expr)(2019))

if __name__ == '__main__':
    main()
