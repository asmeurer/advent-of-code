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

puzzle_input = "6,19,0,5,7,13,1"

def parse_input(text):
    return list(map(int, text.split(',')))

def play(numbers):
    numbers.reverse()
    while len(numbers) < 2020:
        n = numbers[0]
        try:
            n = numbers.index(n, 1)
        except ValueError:
            n = 0
        numbers.insert(0, n)
    numbers.reverse()
    return n

print("Day 15")
print("Part 1")
for i, (input, output) in enumerate(zip(test_input, test_output), 1):
    print("Test input", i)
    numbers = parse_input(input)
    n = play(numbers)
    # print(numbers)
    print(n, "should be", output)
    assert n == output

print("Puzzle input")
numbers = parse_input(puzzle_input)
n = play(numbers)
# print(numbers)
print(n)
