test_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()

puzzle_input = open("day04_input").read().strip()

from collections import Counter

def parse_input(input):
    cards = []
    for line in input.splitlines():
        winning_numbers, card_numbers = line.split("|")
        winning_numbers = [int(n) for n in winning_numbers.split(':')[1].split()]
        card_numbers = [int(n) for n in card_numbers.split()]
        assert len(set(winning_numbers)) == len(winning_numbers)
        assert len(set(card_numbers)) == len(card_numbers)
        cards.append((winning_numbers, card_numbers))
    return cards

def part1(data):
    points = 0
    for winning_numbers, card_numbers in data:
        matching_numbers = set(card_numbers) & set(winning_numbers)
        if matching_numbers:
            points += 2**(len(matching_numbers)-1)
    return points

def part2(data):
    cards = Counter()
    for i, (winning_numbers, card_numbers) in enumerate(data, 1):
        cards[i] += 1
        matching_numbers = set(card_numbers) & set(winning_numbers)
        for j in range(1, len(matching_numbers)+1):
            if i + j <= len(data):
                cards[i + j] += cards[i]

    # print(cards)
    return cards.total()

if __name__ == "__main__":
    print("Day 4")
    print("Part 1")
    print("Test input")
    test_data = parse_input(test_input)
    print(part1(test_data))
    print("Puzzle input")
    puzzle_data = parse_input(puzzle_input)
    print(part1(puzzle_data))

    print("Part 2")
    print("Test input")
    print(part2(test_data))
    print("Puzzle input")
    print(part2(puzzle_data))
