import numpy as np

def split_layers(data, rows, columns):
    layers = len(data)//rows//columns
    a = np.array(list(map(int, data)))

    return a.reshape((layers, columns, rows))


def find_solution(a):
    min_zeros = float('inf')
    min_i = float('nan')
    for i in range(a.shape[0]):
        zeros = np.sum(a[i] == 0)
        if zeros < min_zeros:
            min_zeros = zeros
            min_i = i
    return np.sum(a[min_i] == 1)*np.sum(a[min_i] == 2)



with open('day8-input') as f:
    input = f.read()

if __name__ == '__main__':
    print(find_solution(split_layers(input, 25, 6)))
