input = '172851-675869'

def find():
    lower, upper = map(int, input.split('-'))
    N = 0
    for i in range(lower, upper + 1):
        if increases(i) and has_double(i):
            N += 1
    return N

def increases(n):
    l = str(n)
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

def has_double(n):
    l = str(n)
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            return True
    return False

if __name__ == '__main__':
    print(find())
