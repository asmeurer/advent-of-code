test_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip()

input = open('day01_input').read()

def part1(input):
    nums = []
    for line in input.splitlines():
        digits = [i for i in line if i.isdigit()]
        nums.append(int(digits[0] + digits[-1]))
    return sum(nums)

if __name__ == '__main__':
    print("Day 1")
    print("Part 1")
    print(part1(test_input))
    print(part1(input))
