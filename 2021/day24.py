test_input1 = """
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
"""

input = """
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -4
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -9
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 10
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -9
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x 0
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
"""

def parse_input(data):
    instructions = []
    for line in data.strip().splitlines():
        if line.startswith('inp'):
            instr, a = line.split()
            instructions.append((instr, a))
        else:
            instr, a, b = line.split()
            if b in 'xyzw':
                instructions.append((instr, a, b))
            else:
                instructions.append((instr, a, int(b)))
    return instructions

def run(instructions, inputs):
    vars = {i: 0 for i in 'xyzw'}
    for instruction in instructions:
        if instruction[0] == 'inp':
            res = inputs.pop(0)
            vars[instruction[1]] = res
            continue
        else:
            instr, a, b = instruction
            assert a in list('xyzw')
            A = vars[a]
            B = b if isinstance(b, int) else vars[b]

        if instr == 'add':
            vars[a] = A + B
        elif instr == 'mul':
            vars[a] = A*B
        elif instr == 'div':
            if B == 0:
                raise ZeroDivisionError("div by 0")
            if A*B < 0:
                # Division needs to round towards 0
                vars[a] = -((-A)//(-B))
            else:
                vars[a] = A//B
        elif instr == 'mod':
            if A < 0 or B <= 0:
                raise ZeroDivisionError("mod with nonpositive inputs")
            vars[a] = A % B
        elif instr == 'eql':
            vars[a] = int(A == B)
        else:
            raise ValueError(f"Invalid instruction: {instr!r}")

    return vars

def part1(instructions):
    for N in range(10**14-1, 0, -1):
        inputs = [int(i) for i in str(N)]
        if 0 in inputs:
            continue
        print(N)
        res = run(instructions, inputs)
        if res['z'] == 0:
            return N

print("Day 24")
print("Part 1")
print("Test input")
test_instructions1 = parse_input(test_input1)
for i in range(10):
    test_res1 = run(test_instructions1, [i])
    print(test_res1)
    print(i, ''.join([str(test_res1[i]) for i in 'wxyz']))

print("Puzzle input")
instructions = parse_input(input)
N = part1(instructions)
print(N)
