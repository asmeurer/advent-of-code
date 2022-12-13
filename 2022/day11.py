test_input = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

input = open('day11_input').read()

import re
from dataclasses import dataclass

from sympy import sympify, symbols
import numpy as np
old = symbols('old')

MONKEY = re.compile(r"""
Monkey (\d+):
  Starting items: ((?:\d(?:, )?)+)
  Operation: new = (.*)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)
""".strip())

@dataclass
class Monkey:
    items: list[int]
    operation: object
    test: int
    if_true: int
    if_false: int

def parse_input(data):
    monkeys = []
    for monkey in data.strip().split('\n\n'):
        m = MONKEY.match(monkey)
        n, items, operation, test, if_true, if_false = m.groups()
        assert int(n) == len(monkeys)
        monkeys.append(Monkey([int(i) for i in items.split(', ')],
                              sympify(operation),
                              int(test),
                              int(if_true),
                              int(if_false)
                              ))
    return monkeys

def turn(monkeys, n):
    monkey = monkeys[n]
    k = len(monkey.items)
    for item in monkey.items:
        item = monkey.operation.subs(old, item)
        item //= 3
        if item % monkey.test == 0:
            monkeys[monkey.if_true].items.append(item)
        else:
            monkeys[monkey.if_false].items.append(item)
    monkey.items.clear()
    return k

def round(monkeys):
    N = len(monkeys)
    inspected = np.array([0]*N)
    for n in range(N):
        inspected[n] += turn(monkeys, n)
    return inspected

def part1(monkeys, _debug=False):
    N = len(monkeys)
    inspected = np.array([0]*N)
    for i in range(20):
        inspected += round(monkeys)
        if _debug:
            print("Round", i+1)
            for n, monkey in enumerate(monkeys):
                print(n, monkey.items)
    if _debug: print(inspected)
    inspected.sort()
    return inspected[-1]*inspected[-2]

print("Day 11")
print("Part 1")
print("Test input")
test_monkeys = parse_input(test_input)
print(part1(test_monkeys, _debug=True))
# print(test_monkeys)
print("Puzzle input")
monkeys = parse_input(input)
# print(monkeys)
print(part1(monkeys))
