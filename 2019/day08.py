import numpy as np

def split_layers(data, columns, rows):
    layers = len(data)//rows//columns
    a = np.array(list(map(int, data)))

    return a.reshape((layers, rows, columns))


def find_solution(a):
    min_zeros = float('inf')
    min_i = float('nan')
    for i in range(a.shape[0]):
        zeros = np.sum(a[i] == 0)
        if zeros < min_zeros:
            min_zeros = zeros
            min_i = i
    return np.sum(a[min_i] == 1)*np.sum(a[min_i] == 2)


block = '█'
def inverse(a):
    return '\x1b[7m' + a + '\x1b[0m'

black = block
white = inverse(block)

def show_image(a):
    layers, rows, columns = a.shape
    for r in range(rows):
        for c in range(columns):
            for l in range(layers):
                if a[l, r, c] == 0:
                    print(black, end='')
                    break
                elif a[l, r, c] == 1:
                    print(white, end='')
                    break
        print()


with open('day08-input') as f:
    input = f.read()

test_image = '0222112222120000'

if __name__ == '__main__':
    a = split_layers(test_image, 2, 2)
    print("test image")
    show_image(a)

    a = split_layers(input, 25, 6)
    print(find_solution(a))
    print("Day 8 image")
    show_image(a)
