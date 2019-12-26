import numpy as np

from day13 import prog

def run(input, in_=None, print_=False):
    in_ = in_ or []
    p = prog(input, in_)
    while True:
        try:
            out = next(p)
        except StopIteration:
            return out

def get_arr(x, y):
    A = np.zeros((x, y), dtype=np.int64)
    for i in range(x):
        for j in range(y):
            A[i, j] = run(input, [i, j])
    return A

D = {
    0: '.',
    1: '#',
    }

def print_arr(A):
    S = ''
    for y in range(A.shape[1]):
        for x in range(A.shape[0]):
            S += D[A[x, y]]
        S += '\n'
    print(S)

with open('day19-input') as f:
    input = f.read()

def main():
    print("Day 19 part 1")
    A = get_arr(50, 50)
    print_arr(A)
    print(A.sum())

if __name__ == '__main__':
    main()
