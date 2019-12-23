from collections import defaultdict

from sympy import Add, Symbol

from day14_1 import (parse_input, FUEL, ORE, test_input_3,
                     test_input_4, test_input_5, input)


def _produce(out, rxns, available):
    lhs, rhs = rxns[out]

    for coeff, material in lhs:
        if material == "ORE":
            available["ORE"] += coeff
        else:
            while available[material] < coeff:
                _produce(material, rxns, available)
            available[material] -= coeff
    available[out] += rhs[0]

def produce(out, rxns, available):
    available = defaultdict(int, {k.name: v for k, v in available.items()})
    _rxns = {}
    for o in rxns:
        eq = rxns[o]
        lhs = []
        for term in Add.make_args(eq.lhs):
            coeff, material = term.as_coeff_Mul()
            lhs.append((int(coeff), material.name))
        coeff, material = eq.rhs.as_coeff_Mul()
        rhs = (int(coeff), material.name)
        _rxns[o.name] = (lhs, rhs)

    _produce(out.name, _rxns, available)
    return defaultdict(int, {Symbol(k): v for k, v in available.items()})

def get_fuel_for_ore(rxns, ore):
    available = defaultdict(int)
    available = produce(FUEL, rxns, available)
    print("Finding base multiple")
    available = find_base_multiple(available, rxns)
    doubles = [available]
    while available[ORE] < ore // 2:
        available = double(available)
        doubles.append(available)
    print("Adding doubles")
    while available[ORE] < ore:
        for d in reversed(doubles):
            if d[ORE] + available[ORE] <= ore:
                available = add(available, d)
                # print(available[ORE])
                break
        else:
            break
    print("Doing final production")
    available0 = available.copy()
    while available[ORE] < ore:
        # print(available[ORE], available[FUEL])
        available0, available = available, produce(FUEL, rxns, available)
    return available0[FUEL]

def find_base_multiple(available, rxns):
    while True:
        for i in available:
            if i in [FUEL, ORE]:
                continue
            if available[i] != 0:
                break
        else:
            break
        available = produce(FUEL, rxns, available)
        if available[FUEL] % 1000 == 0:
            print(available[FUEL])
    return available

def double(available):
    return {k: v*2 for k, v in available.items()}

def add(a, b):
    return {k: a[k] + b[k] for k in a}

# def test(rxns):
#     available = defaultdict(int)
#     produce(FUEL, rxns, available)
#     d = double(available)
#     a = add(available, available)
#     produce(FUEL, rxns, available)
#     assert d == a
#     print(d)
#     print(dict(available))
#     assert d == available

def main():
    print("Day14, Part 2, test input 3")
    print("Should give 82892753")
    rxns = parse_input(test_input_3)
    # test(rxns)
    print(get_fuel_for_ore(rxns, 1000000000000))

    print("Day14, Part 2, test input 4")
    print("Should give 5586022")
    print(get_fuel_for_ore(parse_input(test_input_4), 1000000000000))

    print("Day14, Part 2, test input 5")
    print("Should give 460664")
    print(get_fuel_for_ore(parse_input(test_input_5), 1000000000000))

    print("Day14, Part 2")
    print(get_fuel_for_ore(parse_input(input), 1000000000000))

if __name__ == '__main__':
    main()
