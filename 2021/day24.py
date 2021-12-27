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

import itertools

from sympy import symbols, Function, Integer, Symbol, Add, Mul, S, Tuple

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

class FloorDivide(Function):
    @classmethod
    def eval(cls, x, y):
        if x.is_Integer and y.is_Integer:
            if x*y < 0:
                # Division needs to round towards 0
                return -((-x)//(-y))
            else:
                return x//y

        # if isinstance(x, Add):
        #     return x.func(*[FloorDivide(i, y) for i in x.args])



class Mod(Function):
    @classmethod
    def eval(cls, x, y):
        if x.is_Integer and y.is_Integer:
            if x < 0 or y <= 0:
                raise ZeroDivisionError("mod with nonpositive inputs")
            return x % y

        if isinstance(x, Symbol) and y.is_Integer and y > 9:
            return x

        # if isinstance(x, Add):
        #     coeff, rest = x.as_coeff_Add()
        #     if coeff != 0:
        #         return coeff % y + Mod(rest, y)

        if isinstance(x, (Add, Mul)):
            return x.func(*[Mod(i, y) for i in x.args])

        if isinstance(x, Equal):
            return x

class Equal(Function):
    @classmethod
    def eval(cls, x, y):
        if x.is_Integer and y.is_Integer:
            return Integer(x == y)
        if isinstance(x, Symbol) and y.is_Integer and not (1 <= y <= 9):
            return S(0)
        if isinstance(y, Symbol) and x.is_Integer and not (1 <= x <= 9):
            return S(0)

        free_vars = list(x.free_symbols | y.free_symbols)
        possibilities = set()
        if len(free_vars) <= 4:
            for vals in itertools.product(*[range(1, 10)]*len(free_vars)):
                if len(possibilities) == 2:
                    return
                s = list(zip(free_vars, vals))
                x_ = x.subs(s)
                y_ = y.subs(s)
                assert x_.is_Integer and y_.is_Integer, (x_, y_)
                possibilities.add(Integer(x_ == y_))
            if len(possibilities) == 1:
                return possibilities.pop()

def run_sympy(instructions, inputs):
    vars = {i: 0 for i in 'xyzw'}
    input_counter = 0
    for instruction in instructions:
        if instruction[0] == 'inp':
            res = inputs[input_counter]
            input_counter += 1
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
            # if A*B < 0:
            #     # Division needs to round towards 0
            #     vars[a] = -((-A)//(-B))
            # else:
            #     vars[a] = A//B
            vars[a] = FloorDivide(A, B)
        elif instr == 'mod':
            # if A < 0 or B <= 0:
            #     raise ZeroDivisionError("mod with nonpositive inputs")

            vars[a] = Mod(A, B)
            # vars[a] = A % B
        elif instr == 'eql':
            vars[a] = Equal(A, B)
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

def part1_sympy(sympy_z, inputs):
    for vals in itertools.product(*[range(9, 0, -1)]*len(inputs)):
        s = list(zip(inputs, vals))
        res = sympy_z.subs(s)
        assert res.is_Integer
        if res == 0:
            return s

if __name__ == '__main__':
    print("Day 24")
    print("Part 1")
    print("Test input")
    test_instructions1 = parse_input(test_input1)
    for i in range(10):
        test_res1 = run(test_instructions1, [i])
        print(test_res1)
        print(i, ''.join([str(test_res1[i]) for i in 'wxyz']))
    test_sympy_instructions1 = run_sympy(test_instructions1,
                                         Tuple(Symbol('input_0', integer=True, positive=True)))
    print(test_sympy_instructions1)

    print("Puzzle input")
    instructions = parse_input(input)
    # N = part1(instructions)
    # print(N)

    inputs = Tuple(*[symbols('input_%s' % i, integer=True, positive=True) for i in range(14)])
    inputs = inputs.subs({
        # inputs[0]: 9,
        # inputs[1]: 9,
        # inputs[2]: 9,
        # inputs[3]: 9,
        # inputs[4]: 9,
        # inputs[5]: 9,
        # inputs[6]: 9,
        # inputs[7]: 9,
        # inputs[8]: 9,
        # inputs[9]: 9,
        # inputs[10]: 9,
        # inputs[11]: 9,
        # inputs[12]: 9,
        # inputs[13]: 9,
    })
    sympy_instructions = run_sympy(instructions, inputs)
    expr = sympy_instructions['z']
    print(expr)
    free_inputs = sorted(expr.free_symbols, key=lambda i:
                         inputs.index(i))
    print(free_inputs)
    ans = part1_sympy(expr, free_inputs)
    print(ans)
    res = ''.join([str(i) for i in inputs.subs(ans).subs({i: 9 for i in inputs})])
    print(res)
    print(run(instructions, [int(i) for i in res]))
