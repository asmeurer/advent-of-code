test_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip()

input = open("day07_input").read().strip()


from functools import total_ordering
from collections import Counter

def parse_input(input, card_type=1):
    hands = {}
    for line in input.splitlines():
        hand, bid = line.split()
        if card_type == 1:
            hands[Hand(hand)] = int(bid)
        elif card_type == 2:
            hands[Hand2(hand)] = int(bid)
        else:
            raise ValueError("Unknown card type")
    return hands

cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

cards2 = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 12,
    "K": 13,
    "A": 14,
}

@total_ordering
class Card:
    def __init__(self, card, card_type=1):
        if isinstance(card, Card):
            card = card.card
        self.card = card
        self.card_type = card_type
        if card_type == 1:
            self.value = cards[card]
        elif card_type == 2:
            self.value = cards2[card]
        else:
            raise ValueError("Unknown card type")

    def __repr__(self):
        return self.card

    def __eq__(self, other):
        if isinstance(other, str):
            return self.card == other
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __hash__(self):
        return hash(self.card)

hand_types = {
    "five of a kind": 7,
    "four of a kind": 6,
    "full house": 5,
    "three of a kind": 4,
    "two pair": 3,
    "one pair": 2,
    "high card": 1,
}

@total_ordering
class Hand:
    def __init__(self, cards):
        self.cards = tuple([Card(card) for card in cards])

    def __contains__(self, card):
        return card in self.cards

    def __repr__(self):
        return " ".join([str(card) for card in self.cards])

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        return (hand_types[self.hand_type], self.cards) < (hand_types[other.hand_type], other.cards)

    def __hash__(self):
        return hash(self.cards)

    @property
    def hand_type(self):
        card_nums = Counter(self.cards)
        match sorted(card_nums.values()):
            case [5]: return "five of a kind"
            case [1, 4]: return "four of a kind"
            case [2, 3]: return "full house"
            case [1, 1, 3]: return "three of a kind"
            case [1, 2, 2]: return "two pair"
            case [1, 1, 1, 2]: return "one pair"
            case [1, 1, 1, 1, 1]: return "high card"
            case _: raise ValueError(f"Unknown hand type {self}")

class Hand2(Hand):
    def __init__(self, cards):
        self.cards = tuple([Card(card, card_type=2) for card in cards])

    @property
    def hand_type(self):
        card_nums = Counter(self.cards)
        jokers = card_nums.pop("J", 0)
        match (jokers, sorted(card_nums.values())):
            case (0, _): return super().hand_type
            case (1, [4]): return "five of a kind"
            case (1, [1, 3]): return "four of a kind"
            case (1, [2, 2]): return "full house"
            case (1, [1, 1, 2]): return "three of a kind"
            case (1, [1, 1, 1, 1]): return "one pair"
            case (2, [3]): return "five of a kind"
            case (2, [1, 2]): return "four of a kind"
            case (2, [1, 1, 1]): return "three of a kind"
            case (3, [2]): return "five of a kind"
            case (3, [1, 1]): return "four of a kind"
            case (4, [1]): return "five of a kind"
            case (5, []): return "five of a kind"
            case _: raise ValueError(f"Unknown hand type {self}")

def score(hands):
    return sum(i*hands[hand] for i, hand in enumerate(sorted(hands), 1))

if __name__ == "__main__":
    print("Day 7")
    print("Part 1")
    print("Test input")
    test_hands = parse_input(test_input)
    print(test_hands)
    for hand in test_hands:
        print(hand, hand.hand_type)
    print(sorted(test_hands))
    print(score(test_hands))
    print("Puzzle input")
    hands = parse_input(input)
    print(score(hands))

    print("Part 2")
    print("Test input")
    test_hands2 = parse_input(test_input, card_type=2)
    print(test_hands2)
    for hand in test_hands2:
        print(hand, hand.hand_type)
    print(sorted(test_hands2))
    print(score(test_hands2))
    print("Puzzle input")
    hands2 = parse_input(input, card_type=2)
    # for hand in sorted(hands2):
    #     if "J" in hand:
    #         print(hand, hand.hand_type)
    print(score(hands2))
