test_input = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip()

test_input_no_wildcards = """
#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1
""".strip()

from functools import lru_cache

puzzle_input = open('day12_input').read().strip()

def parse_input(input):
    all_springs = []
    for line in input.splitlines():
        springs, nums = line.split()
        nums = tuple([int(n) for n in nums.split(',')])
        all_springs.append((springs, nums))
    return all_springs

@lru_cache(maxsize=None)
def arrangements(springs, nums, prev=''):
    if not nums:
        if '#' in springs:
            return 0
        return 1
    if not springs:
        if nums not in ((), (0,)):
            return 0
        else:
            return 1
    n = nums[0]
    c = springs[0]
    total = 0
    if n == 0:
        if c == '#':
            return 0
        else:
            total += arrangements(springs[1:], nums[1:], '.')
    else:
        if c == '.':
            if prev == '#':
                return 0
            total += arrangements(springs[1:], nums, '.')
        else:
            if c == '?' and prev != '#':
                total += arrangements(springs[1:], nums, '.')
            n -= 1
            total += arrangements(springs[1:], (n,) + nums[1:], '#')
    return total

def unfold(springs, nums, times=5):
    return '?'.join(times*[springs]), times*nums

def part1(all_springs, verbose=2):
    totals = []
    for i, (springs, nums) in enumerate(all_springs):
        if verbose: print(f"Springs ({i+1}/{len(all_springs)}): {springs}, nums: {nums}")
        n = 0
        n = arrangements(springs, nums)
        if verbose: print(f"Total: {n}")
        totals.append(n)
    return sum(totals)

def part2(all_springs, verbose=1):
    unfolded_all_springs = [unfold(springs, nums) for springs, nums in
                            all_springs]
    return part1(unfolded_all_springs, verbose=verbose)

if __name__ == '__main__':
    print("Day 12")
    print("Part 1")
    print("Test input (no wildcards)")
    test_all_springs_no_wildcards = parse_input(test_input_no_wildcards)
    print(part1(test_all_springs_no_wildcards))
    print("Test input")
    test_all_springs = parse_input(test_input)
    print(part1(test_all_springs))
    print("Puzzle input")
    puzzle_all_springs = parse_input(puzzle_input)
    print(part1(puzzle_all_springs, verbose=False))
    print("Part 2")
    print("Test input")
    print(part2(test_all_springs))
    print("Puzzle input")
    print(part2(puzzle_all_springs))
