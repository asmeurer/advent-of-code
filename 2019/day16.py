from itertools import cycle, islice

import numpy as np
from numba import njit

def get_pattern(n, l):
    c = cycle([0]*n + [1]*n + [0]*n + [-1]*n)
    next(c)
    return np.array(list(islice(c, l)))

@njit
def dot(a, b):
    A = 0
    for i, j in zip(a, b):
        A += i*j
    return np.abs(A) % 10

def run_n(signal, n):
    signal = np.array([int(i) for i in signal])
    l = signal.shape[0]
    patterns = np.zeros((l,)*2, dtype=np.int64)
    for k in range(1, len(signal) + 1):
        patterns[k-1] = get_pattern(k, l)

    return ''.join([str(i) for i in _run_n(signal, patterns, n)])

@njit
def _run_n(signal, patterns, n):
    for i in range(n):
        signal = _phase(signal, patterns)
    return signal

@njit
def _phase(signal, patterns):
    res = np.zeros(signal.shape, dtype=np.int64)
    for n in range(len(signal)):
        res[n] = dot(signal, patterns[n])
    return res

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
        p = run_n(p, 1)
        print(p)

    print("test input 2")
    print("Should give 24176176")
    p = run_n(test_input_2, 100)
    print(p[:8])

    print("test input 2")
    print("Should give 73745418")
    p = run_n(test_input_3, 100)
    print(p[:8])

    print("test input 2")
    print("Should give 52432133")
    p = run_n(test_input_4, 100)
    print(p[:8])

    print("Day 16 part 1")
    p = run_n(input, 100)
    print(p[:8])

    print("Day 16 part 2")
    real_input = run_n(input, 10000)
    print(real_input)

if __name__ == '__main__':
    main()
