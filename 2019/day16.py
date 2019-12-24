from itertools import cycle
import numpy as np

def get_pattern(n):
    c = cycle([0]*n + [1]*n + [0]*n + [-1]*n)
    next(c)
    return c

def dot(a, b):
    A = 0
    for i, j in zip(a, b):
        A += i*j
    return int(str(A)[-1])

def phase(signal):
    s = [int(i) for i in signal]
    res = []
    for n in range(1, len(signal) + 1):
        res.append(dot(s, get_pattern(n)))
    return ''.join([str(i) for i in res])

test_input_1 = '12345678'
test_input_2 = '80871224585914546619083218645595'
test_input_3 = '19617804207202209144916044189917'
test_input_4 = '69317163492948606335995924319873'

input = '59701570675760924481468012067902478812377492613954566256863227624090726538076719031827110112218902371664052147572491882858008242937287936208269895771400070570886260309124375604950837194732536769939795802273457678297869571088110112173204448277260003249726055332223066278888042125728226850149451127485319630564652511440121971260468295567189053611247498748385879836383604705613231419155730182489686270150648290445732753180836698378460890488307204523285294726263982377557287840630275524509386476100231552157293345748976554661695889479304833182708265881051804444659263862174484931386853109358406272868928125418931982642538301207634051202072657901464169114'
def main():
    print("Test input 1")
    print("Should output")
    print("""\
48226158
34040438
03415518
01029498
""")
    p = test_input_1
    for i in range(4):
        p = phase(p)
        print(p)

    print("test input 2")
    print("Should give 24176176")
    p = test_input_2
    for i in range(100):
        p = phase(p)
    print(p[:8])

    print("test input 2")
    print("Should give 73745418")
    p = test_input_3
    for i in range(100):
        p = phase(p)
    print(p[:8])

    print("test input 2")
    print("Should give 52432133")
    p = test_input_4
    for i in range(100):
        p = phase(p)
    print(p[:8])

    print("Day 16 part 1")
    p = input
    for i in range(100):
        p = phase(p)
    print(p[:8])


if __name__ == '__main__':
    main()
