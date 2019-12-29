import numpy as np

def asarray(I):
    lines = I.splitlines()
    return np.array(lines, "S").view("S1").reshape((len(lines), -1))

with open('day20-input') as f:
    input = f.read()

def main():
    pass

if __name__ == '__main__':
    main()
