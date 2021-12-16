test_input1 = "D2FE28"
test_input2 = "38006F45291200"
test_input3 = "EE00D40C823060"
test_input4 = "8A004A801A8002F478"
test_input5 = "620080001611562C8802118E34"
test_input6 = "C0015000016115A2E0802F182340"
test_input7 = "A0016C880162017C3686B18A3D4780"

test_input8 = "C200B40A82"
test_input9 = "04005AC33890"
test_input10 = "880086C3E88112"
test_input11 = "CE00C43D881120"
test_input12 = "D8005AC2A8F0"
test_input13 = "F600BC2D8F"
test_input14 = "9C005AC2F8F0"
test_input15 = "9C0141080250320F1802104A08"

input = "E20D7880532D4E551A5791BD7B8C964C1548CB3EC1FCA41CC00C6D50024400C202A65C00C20257C008AF70024C00810039C00C3002D400A300258040F200D6040093002CC0084003FA52DB8134DE620EC01DECC4C8A5B55E204B6610189F87BDD3B30052C01493E2DC9F1724B3C1F8DC801E249E8D66C564715589BCCF08B23CA1A00039D35FD6AC5727801500260B8801F253D467BFF99C40182004223B4458D2600E42C82D07CC01D83F0521C180273D5C8EE802B29F7C9DA1DCACD1D802469FF57558D6A65372113005E4DB25CF8C0209B329D0D996C92605009A637D299AEF06622CE4F1D7560141A52BC6D91C73CD732153BF862F39BA49E6BA8C438C010E009AA6B75EF7EE53BBAC244933A48600B025AD7C074FEB901599A49808008398142013426BD06FA00D540010C87F0CA29880370E21D42294A6E3BCF0A080324A006824E3FCBE4A782E7F356A5006A587A56D3699CF2F4FD6DF60862600BF802F25B4E96BDD26049802333EB7DDB401795FC36BD26A860094E176006A0200FC4B8790B4001098A50A61748D2DEDDF4C6200F4B6FE1F1665BED44015ACC055802B23BD87C8EF61E600B4D6BAD5800AA4E5C8672E4E401D0CC89F802D298F6A317894C7B518BE4772013C2803710004261EC318B800084C7288509E56FD6430052482340128FB37286F9194EE3D31FA43BACAF2802B12A7B83E4017E4E755E801A2942A9FCE757093005A6D1F803561007A17C3B8EE0008442085D1E8C0109E3BC00CDE4BFED737A90DC97FDAE6F521B97B4619BE17CC01D94489E1C9623000F924A7C8C77EA61E6679F7398159DE7D84C015A0040670765D5A52D060200C92801CA8A531194E98DA3CCF8C8C017C00416703665A2141008CF34EF8019A080390962841C1007217C5587E60164F81C9A5CE0E4AA549223002E32BDCEA36B2E100A160008747D8B705C001098DB13A388803F1AE304600"

from collections import namedtuple
from math import prod

import black

hex_map = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def parse_input(data):
    res = [hex_map[i] for i in data]
    return ''.join(res)

literal_packet = namedtuple('literal_packet', ['version', 'type', 'val'])
operator_packet = namedtuple('operator_packet', ['version', 'type', 'ID', 'L', 'rest'])

def parse_bits(bits):
    packet = []
    if not bits:
        return packet
    i = 0
    version = int(bits[:3], 2)
    typ = int(bits[3:6], 2)
    i = 6
    if typ == 4:
        parts = []
        while bits[i] == '1':
            parts.append(bits[i+1:i+5])
            i += 5
        parts.append(bits[i+1:i+5])
        i += 5
        val = int(''.join(parts), 2)
        packet.append(literal_packet(version, typ, val))
        if '1' in bits[i:]:
            packet.extend(parse_bits(bits[i:]))
    else:
        ID = int(bits[i])
        i += 1
        if ID == 0:
            L = int(bits[i:i+15], 2)
            i += 15
            rest = parse_bits(bits[i:i+L])
        elif ID == 1:
            L = int(bits[i:i+11], 2)
            i += 11
            more = parse_bits(bits[i:])
            rest, more = more[:L], more[L:]
            packet.extend(more)
        else:
            raise ValueError(f"Unexpected ID: {ID}")
        packet.append(operator_packet(version, typ, ID, L, rest))
        if ID == 0 and '1' in bits[i+L:]:
            packet.extend(parse_bits(bits[i+L:]))

    return packet

# https://stackoverflow.com/a/65298131/161801
def pprint(x):
    print(black.format_str(repr(x), mode=black.Mode()))

def version_sum(packets):
    A = 0
    for p in packets:
        A += p[0]
        if isinstance(p, operator_packet):
            A += version_sum(p.rest)
    return A

operators = {
    0: lambda *x: sum(x),
    1: lambda *x: prod(x),
    2: min,
    3: max,
    5: lambda x, y: int(x > y),
    6: lambda x, y: int(x < y),
    7: lambda x, y: int(x == y),
}

def evaluate(packet):
    if isinstance(packet, literal_packet):
        return packet.val
    elif isinstance(packet, operator_packet):
        return operators[packet.type](*[evaluate(p) for p in packet.rest])
    else:
        raise TypeError(f"Invalid packet type: {type(packet)}")

print("Day 16")
print("Part 1")
print("Test inputs")
test_bits1 = parse_input(test_input1)
test_bits2 = parse_input(test_input2)
test_bits3 = parse_input(test_input3)
test_bits4 = parse_input(test_input4)
test_bits5 = parse_input(test_input5)
test_bits6 = parse_input(test_input6)
test_bits7 = parse_input(test_input7)
test_bits8 = parse_input(test_input8)
test_bits9 = parse_input(test_input9)
test_bits10 = parse_input(test_input10)
test_bits11 = parse_input(test_input11)
test_bits12 = parse_input(test_input12)
test_bits13 = parse_input(test_input13)
test_bits14 = parse_input(test_input14)
test_bits15 = parse_input(test_input15)

test_packets1 = parse_bits(test_bits1)
print(test_packets1)
test_packets2 = parse_bits(test_bits2)
print(test_packets2)
test_packets3 = parse_bits(test_bits3)
print(test_packets3)
print(test_input4)
test_packets4 = parse_bits(test_bits4)
pprint(test_packets4)
print(version_sum(test_packets4))
print(test_input5)
test_packets5 = parse_bits(test_bits5)
pprint(test_packets5)
print(version_sum(test_packets5))
print(test_input6)
test_packets6 = parse_bits(test_bits6)
pprint(test_packets6)
print(version_sum(test_packets6))
print(test_input7)
test_packets7 = parse_bits(test_bits7)
pprint(test_packets7)
print(version_sum(test_packets7))

print("Puzzle input")
bits = parse_input(input)
packets = parse_bits(bits)
pprint(packets)
print(version_sum(packets))

print("Part 2")
print("Test input")

print(test_input8)
test_packets8 = parse_bits(test_bits8)
pprint(test_packets8)
test_packets8_val = evaluate(test_packets8[0])
print(test_packets8_val)

print(test_input9)
test_packets9 = parse_bits(test_bits9)
pprint(test_packets9)
test_packets9_val = evaluate(test_packets9[0])
print(test_packets9_val)

print(test_input10)
test_packets10 = parse_bits(test_bits10)
pprint(test_packets10)
test_packets10_val = evaluate(test_packets10[0])
print(test_packets10_val)

print(test_input11)
test_packets11 = parse_bits(test_bits11)
pprint(test_packets11)
test_packets11_val = evaluate(test_packets11[0])
print(test_packets11_val)

print(test_input12)
test_packets12 = parse_bits(test_bits12)
pprint(test_packets12)
test_packets12_val = evaluate(test_packets12[0])
print(test_packets12_val)

print(test_input13)
test_packets13 = parse_bits(test_bits13)
pprint(test_packets13)
test_packets13_val = evaluate(test_packets13[0])
print(test_packets13_val)

print(test_input14)
test_packets14 = parse_bits(test_bits14)
pprint(test_packets14)
test_packets14_val = evaluate(test_packets14[0])
print(test_packets14_val)

print(test_input15)
test_packets15 = parse_bits(test_bits15)
pprint(test_packets15)
test_packets15_val = evaluate(test_packets15[0])
print(test_packets15_val)

print("Puzzle input")
packets_val = evaluate(packets[0])
print(packets_val)
