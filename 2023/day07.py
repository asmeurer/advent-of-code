test_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip()

input = open("day07_input").read().strip()


from functools import total_ordering

def parse_input(input):
    hands = {}
    for line in input.splitlines():
        hand, bid = line.split()
        hands[Hand(*hand)] = int(bid)
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

@total_ordering
class Card:
    def __init__(self, card):
        if isinstance(card, Card):
            card = card.card
        self.card = card
        self.value = cards[card]

    def __repr__(self):
        return self.card

    def __eq__(self, other):
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
    def __init__(self, *cards):
        self.cards = tuple([Card(card) for card in cards])

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
        if all(card == self.cards[0] for card in self.cards):
            return "five of a kind"
        elif len(set(self.cards)) == 2:
            match self.cards.count(self.cards[0]):
                case 1 | 4: return "four of a kind"
                case 2 | 3: return "full house"
        elif len(set(self.cards)) == 3:
            match self.cards.count(self.cards[0]):
                case 3: return "three of a kind"
                case 2: return "two pair"
                case 1:
                    match self.cards.count(self.cards[1]):
                        case 3 | 1: return "three of a kind"
                        case 2: return "two pair"
        elif len(set(self.cards)) == 4:
            return "one pair"
        else:
            return "high card"


def part1(hands):
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
    print(part1(test_hands))
    print("Puzzle input")
    hands = parse_input(input)
    print(part1(hands))
