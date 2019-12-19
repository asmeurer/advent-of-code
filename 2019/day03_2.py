import sys

from numba import njit
import numpy as np

from day3_1 import input1, input2

def wire(input, shape=(10000, 10000)):
    I = np.zeros(shape, dtype=np.int64)
    o = [shape[0]//2, shape[1]//2]
    val = 0
    for i in input:
        dir, amount = i[0], i[1:]
        amount = int(amount)
        if dir == 'R':
            if amount + o[1] >= shape[1]:
                raise ValueError(amount, o, dir)
            s = (o[0], slice(o[1], amount + o[1] + 1))
            o[1] += amount
            V = np.arange(val, val + amount + 1)
        elif dir == 'L':
            if o[1] - amount < 0:
                raise ValueError(amount, o, dir)
            s = (o[0], slice(o[1] - amount, o[1] + 1))
            o[1] -= amount
            V = np.arange(val + amount, val - 1, -1)
        elif dir == 'D':
            if o[0] + amount >= shape[0]:
                raise ValueError(amount, o, dir)
            s = (slice(o[0], o[0] + amount + 1), o[1])
            o[0] += amount
            V = np.arange(val, val + amount + 1)
        elif dir == 'U':
            if o[0] - amount < 0:
                raise ValueError(amount, o, dir)
            s = (slice(o[0] - amount, o[0] + 1), o[1])
            o[0] -= amount
            V = np.arange(val + amount, val - 1, -1)
        else:
            raise ValueError(dir)
        I[s] = V
        val += amount
    return I

@njit
def dist(I1, I2):
    shape = I1.shape
    assert I2.shape == shape
    center = (shape[0]//2, shape[1]//2)
    A = I1 * I2
    A[center] = 0
    x, y = np.where(A != 0)
    m = sys.maxsize
    for i, j in zip(x, y):
        d = I1[i, j] + I2[i, j]
        if d < m:
            m = d
    return m

if __name__ == '__main__':
    I1 = wire(input1.split(','), (20000, 30000))
    I2 = wire(input2.split(','), (20000, 30000))
    print(dist(I1, I2))
