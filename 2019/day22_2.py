from sympy import symbols, lambdify, Poly, mod_inverse

import numpy as np

import re

x = symbols('x')

def parse_input(I):
    expr = x

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
    return expr

def invert(expr, p):
    a, b = Poly(expr, x).coeffs()
    return mod_inverse(a, p)*(x - b)

def iterate_n_times_mod_p(expr, n, p):
    # a*x + b iterated by x n times (mod p) is a**n*x + (a**(n - 1) + a**(n -
    # 2) + ... + a + 1)*b = a**n*x + (a**n - 1)/(a - 1)*b
    a, b = Poly(expr, x).coeffs()
    a_n = pow(a, n, p)
    iterated = (a_n*x + (a_n - 1)*mod_inverse(a - 1, p)*b) % p
    return iterated

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

prime = 119315717514047
times = 101741582076661

with open('day22-input') as f:
    input = f.read()

def main():
    print("Day 22, test input 1")
    expr = parse_input(test_input_1) % 10
    print(expr)
    print(lambdify(x, expr)(test_answer_1))
    print(lambdify(x, expr)(2))
    print()

    print("Day 22, test input 2")
    expr = parse_input(test_input_2) % 10
    print(expr)
    print(lambdify(x, expr)(test_answer_2))
    print()

    print("Day 22, test input 3")
    expr = parse_input(test_input_3) % 10
    print(expr)
    print(lambdify(x, expr)(test_answer_3))
    print()

    print("Day 22, part 1")
    expr = parse_input(input)
    expr_ = expr % 10007
    print(expr_)
    print(lambdify(x, expr_)(2019))

    print("Day 22, part 1")
    expr_ = invert(expr, prime)
    iterated = iterate_n_times_mod_p(expr_, times, prime)
    print(iterated)
    print(lambdify(x, iterated)(2020))

if __name__ == '__main__':
    main()
