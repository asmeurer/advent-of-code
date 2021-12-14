test_input = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

input = """
FSHBKOOPCFSFKONFNFBB

FO -> K
FF -> H
SN -> C
CC -> S
BB -> V
FK -> H
PC -> P
PH -> N
OB -> O
PV -> C
BH -> B
HO -> C
VF -> H
HB -> O
VO -> N
HK -> N
OF -> V
PF -> C
KS -> H
KV -> F
PO -> B
BF -> P
OO -> B
PS -> S
KC -> P
BV -> K
OC -> B
SH -> C
SF -> P
NH -> C
BS -> C
VH -> F
CH -> S
BC -> B
ON -> K
FH -> O
HN -> O
HS -> C
KK -> V
OK -> K
VC -> H
HV -> F
FS -> H
OV -> P
HF -> F
FB -> O
CK -> O
HP -> C
NN -> V
PP -> F
FC -> O
SK -> N
FN -> K
HH -> F
BP -> O
CP -> K
VV -> S
BO -> N
KN -> S
SB -> B
SC -> H
OS -> S
CF -> K
OP -> P
CO -> C
VK -> C
NB -> K
PB -> S
FV -> B
CS -> C
HC -> P
PK -> V
BK -> P
KF -> V
NS -> P
SO -> C
CV -> P
NP -> V
VB -> F
KO -> C
KP -> F
KH -> N
VN -> S
NO -> P
NF -> K
CB -> H
VS -> V
NK -> N
KB -> C
SV -> F
NC -> H
VP -> K
PN -> H
OH -> K
CN -> N
BN -> F
NV -> K
SP -> S
SS -> K
FP -> S
"""

from collections import Counter

def parse_input(data):
    template, _rules = data.strip().split('\n\n')
    rules = dict([i.split(' -> ') for i in _rules.splitlines()])
    element = Element.fromiter(template)
    return element, rules

class Element:
    def __init__(self, name, next=None):
        self.name = name
        self.next = next

    def __repr__(self):
        return f"Element({self.name})"

    @classmethod
    def fromiter(self, elems):
        elements = [Element(i) for i in elems]

        for i, j in zip(elements, elements[1:]):
            i.next = j

        return elements[0]

    def copy(self):
        return Element.fromiter(self.tostr())

    def tostr(self):
        element = self
        l = []
        while element:
            l.append(element.name)
            element = element.next
        return ''.join(l)

def apply_rules(element, rules):
    first_e = e = element.copy()

    while e.next:
        if e.name + e.next.name in rules:
            E = Element(rules[e.name + e.next.name], e.next)
            e.next, e = E, e.next
        else:
            e = e.next
    return first_e

def apply_rules_n_times(element, rules, n):
    for i in range(n):
        element = apply_rules(element, rules)
    return element

def part1(element):
    c = Counter(element.tostr())
    (_, M), *_, (_, m) = c.most_common()
    return M - m

print("Day 14")
print("Part 1")
print("Test input")
test_e, test_rules = parse_input(test_input)
print(test_e.tostr())
print(test_rules)
test_e1 = apply_rules(test_e, test_rules)
print(test_e1.tostr())
assert test_e1.tostr() == 'NCNBCHB'
test_e2 = apply_rules(test_e1, test_rules)
print(test_e2.tostr())
assert test_e2.tostr() == 'NBCCNBBBCBHCB'
test_e3 = apply_rules(test_e2, test_rules)
print(test_e3.tostr())
assert test_e3.tostr() == 'NBBBCNCCNBBNBNBBCHBHHBCHB'
test_e4 = apply_rules(test_e3, test_rules)
print(test_e4.tostr())
assert test_e4.tostr() == 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
test_e5 = apply_rules(test_e4, test_rules)
print('test step 5', test_e5.tostr())
test_e10 = apply_rules_n_times(test_e, test_rules, 10)
print(test_e10.tostr())
print(part1(test_e10))

print("Puzzle input")
e, rules = parse_input(input)
e10 = apply_rules_n_times(e, rules, 10)
# print(e10.tostr())
print(part1(e10))
