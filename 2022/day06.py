test_inputs = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]

input = open('day06_input').read()

def get_marker(text, n):
    i = 0
    while True:
        if len(set(text[i:i+n])) == n:
            return i + n
        i += 1

def part1(text):
    return get_marker(text, 4)

def part2(text):
    return get_marker(text, 14)

print("Day 6")
print("Part 1")
print("Test inputs")
for text in test_inputs:
    print(part1(text))
print("Puzzle input")
print(part1(input))

print("Part 2")
print("Test inputs")
for text in test_inputs:
    print(part2(text))
print("Puzzle input")
print(part2(input))
