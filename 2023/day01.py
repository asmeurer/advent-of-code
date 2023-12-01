test_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip()

test_input2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip()

input = open('day01_input').read()

import re

def part1(input):
    nums = []
    for line in input.splitlines():
        digits = [i for i in line if i.isdigit()]
        nums.append(int(digits[0] + digits[-1]))
    return sum(nums)

digits = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
    **{str(i): i for i in range(10)}
}

PATTERN = re.compile('|'.join(digits))
REV_PATTERN = re.compile(PATTERN.pattern[::-1])

def part2(input):
    nums = []
    for line in input.splitlines():
        first_word = PATTERN.search(line).group()
        last_word = REV_PATTERN.search(line[::-1]).group()[::-1]
        num = 10*digits[first_word] + digits[last_word]
        nums.append(num)
    return sum(nums)

if __name__ == '__main__':
    print("Day 1")
    print("Part 1")
    print(part1(test_input))
    print(part1(input))

    print("Part 2")
    print(part2(test_input2))
    print(part2(input))
