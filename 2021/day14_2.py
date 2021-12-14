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
    return template, rules


def apply_rule(a, b, rules, n):
    memo = {}
    # apply_rule does not count b
    def _apply_rule(a, b, d=1):
        if d == n:
            return Counter(a + rules[a+b])
        if (a, b, d) in memo:
            return memo[a, b, d]
        c = Counter()
        memo[a, b, d] = res = c + _apply_rule(a, rules[a+b], d+1) + _apply_rule(rules[a+b], b, d+1)
        return res

    return _apply_rule(a, b)

def apply_rules(template, rules, n):
    c = Counter(template[-1])
    for a, b in zip(template, template[1:]):
        c += apply_rule(a, b, rules, n)
    return c

def part2(c):
    (_, M), *_, (_, m) = c.most_common()
    return M - m

print("Day 14")
print("Part 1")
print("Test input")
test_template, test_rules = parse_input(test_input)
print(test_template)
print(test_rules)
test_c1 = apply_rules(test_template, test_rules, 1)
assert test_c1 == Counter('NCNBCHB')
test_c2 = apply_rules(test_template, test_rules, 2)
assert test_c2 == Counter('NBCCNBBBCBHCB')
test_c3 = apply_rules(test_template, test_rules, 3)
assert test_c3 == Counter('NBBBCNCCNBBNBNBBCHBHHBCHB')
test_c4 = apply_rules(test_template, test_rules, 4)
assert test_c4 == Counter('NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')
print("Doing step 5")
test_c5 = apply_rules(test_template, test_rules, 5)
print('step 5 computed', test_c5)
print('step 5 actual', Counter('NBBNBBNBBBNBBNBBCNCCNBBBCCNBCNCCNBBNBBNBBNBBNBBNBNBBNBBNBBNBBNBBCHBHHBCHBHHNHCNCHBCHBNBBCHBHHBCHB'))
assert sum(test_c5.values()) == 97, sum(test_c5.values())
test_c10 = apply_rules(test_template, test_rules, 10)
print(test_c10)
assert test_c10['B'] == 1749
assert test_c10['H'] == 161

test_c40 = apply_rules(test_template, test_rules, 40)
print(test_c40)
assert test_c40['B'] == 2192039569602
assert test_c40['H'] == 3849876073
test_res = part2(test_c40)
print(test_res)
assert test_res == 2188189693529

print("Puzzle input")
template, rules = parse_input(input)
c40 = apply_rules(template, rules, 40)
print(c40)
res = part2(c40)
print(res)
