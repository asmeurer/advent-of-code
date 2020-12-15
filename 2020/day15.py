test_input = [
    "0,3,6",
    "1,3,2",
    "2,1,3",
    "1,2,3",
    "2,3,1",
    "3,2,1",
    "3,1,2",
]

test_output = [
    436,
    1,
    10,
    27,
    78,
    438,
    1836,
]

test_output2 = [
    175594,
    2578,
    3544142,
    261214,
    6895259,
    18,
    362,
]

puzzle_input = "6,19,0,5,7,13,1"

def parse_input(text):
    return list(map(int, text.split(',')))

def parse_input2(text):
    return {int(n): i for i, n in enumerate(text.split(','), 1)}

def play(numbers, k=2020):
    numbers.reverse()
    while len(numbers) < k:
        n = numbers[0]
        try:
            n = numbers.index(n, 1)
        except ValueError:
            n = 0
        numbers.insert(0, n)
    numbers.reverse()
    return n

def play2(numbers, k):
    n = len(numbers)
    i = [i for i in numbers if numbers[i] == n][0]
    numbers = {j: n for j, n in numbers.items() if j != i}
    while n < k:
        if n % (k//10) == 0:
            print(f"{n/k*100}%")
        if i in numbers and numbers[i] < n:
            i2 = n - numbers[i]
        else:
            i2 = 0
        numbers[i] = n
        n += 1
        i = i2
    # print(numbers)
    return i

print("Day 15")
print("Part 1")
for i, (input, output) in enumerate(zip(test_input, test_output), 1):
    print("Test input", i)
    numbers = parse_input(input)
    n = play(numbers)
    print(numbers)
    print(n, "should be", output)
    assert n == output

print("Puzzle input")
numbers = parse_input(puzzle_input)
n = play(numbers)
# print(numbers)
print(n)

print("Part 2")
for i, (input, output) in enumerate(zip(test_input, test_output), 1):
    print("Test input", i)
    numbers = parse_input2(input)
    n = play2(numbers, 2020)
    print(n, "should be", output)
    assert n == output

for i, (input, output) in enumerate(zip(test_input, test_output2), 1):
    print("Test input", i)
    numbers = parse_input2(input)
    n = play2(numbers, 30000000)
    print(n, "should be", output)
    assert n == output

print("Puzzle input")
numbers = parse_input2(puzzle_input)
n = play2(numbers, 2020)
print(n)
n = play2(numbers, 30000000)
print(n)
