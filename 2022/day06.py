test_inputs = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]

input = open('day06_input').read()

def part1(text):
    i = 0
    while True:
        if len(set(text[i:i+4])) == 4:
            return i + 4
        i += 1

print("Day 6")
print("Part 1")
print("Test inputs")
for text in test_inputs:
    print(part1(text))
print("Puzzle input")
print(part1(input))
