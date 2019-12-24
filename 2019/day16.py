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

def main():
    print("Test input")
    print("Should output")
    print("""
48226158
34040438
03415518
01029498
""")
    p = '12345678'
    for i in range(4):
        p = phase(p)
        print(p)

if __name__ == '__main__':
    main()
