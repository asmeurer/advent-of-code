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
from functools import lru_cache
import math

import numpy as np

from sympy import (symbols, Function, Integer, Symbol, Add, Mul, S, Tuple,
                   cse, lambdify)
from sympy.printing.lambdarepr import LambdaPrinter

from numba import njit

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

        if y == 1:
            return x
        # if isinstance(x, Add):
        #     return x.func(*[FloorDivide(i, y) for i in x.args])



class Mod(Function):
    @classmethod
    def eval(cls, x, y):
        if x.is_Integer and y.is_Integer:
            if x < 0 or y <= 0:
                raise ZeroDivisionError("mod with nonpositive inputs")
            return x % y

        if isinstance(x, Symbol) and 'input' in x.name and y.is_Integer and y > 9:
            return x

        # if isinstance(x, Add):
        #     coeff, rest = x.as_coeff_Add()
        #     if coeff != 0:
        #         return coeff % y + Mod(rest, y)

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
        if len(free_vars) <= 0:
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

class CustomPrinter(LambdaPrinter):
    def _print_Equal(self, expr):
        x, y = expr.args
        return f"int({self._print(x)} == {self._print(y)})"

    def _print_FloorDivide(self, expr):
        x, y = expr.args
        return f"({self._print(x)} // {self._print(y)})"

    def _print_Mod(self, expr):
        x, y = expr.args
        return f"({self._print(x)} % {self._print(y)})"

# modules = {"Equal": lambda x, y: int(x == y),
#            "FloorDivide": lambda x, y: x//y,
#            "Mod": lambda x, y: x % y,
#            }


def inner_lambdify(variables, expr):
    # Cache only the free variables in the subexpression. Otherwise caching
    # cannot work.
    free_vars = sorted(expr.free_symbols, key=variables.index)
    mapping = [variables.index(i) for i in free_vars]

    f = lru_cache(None)(njit(lambdify(free_vars, expr, printer=CustomPrinter)))
    return lambda *vars: f(*[vars[i] for i in mapping])

# https://stackoverflow.com/questions/11144513/cartesian-product-of-x-and-y-array-points-into-single-array-of-2d-points
def cartesian_product(*arrays):
    if len(arrays) == 0:
        return np.empty((1, 0))
    la = len(arrays)
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)


@njit
def boolallvals2(f, x1, x2):
    res = np.zeros((2, 2), dtype=np.int64)
    for i1 in x1:
        for i2 in x2:
            res[int(f(i1, i2))] = np.array([i1, i2])
    return res


@njit
def boolallvals4(f, x1, x2, x3, x4):
    res = np.zeros((2, 4), dtype=np.int64)
    for i1 in x1:
        for i2 in x2:
            for i3 in x3:
                for i4 in x4:
                    res[int(f(i1, i2, i3, i4))] = np.array([i1, i2, i3, i4])
    return res

@njit
def allvals_final3(f, x1, x2, x3):
    for i1 in x1:
        for i2 in x2:
            for i3 in x3:
                if f(i1, i2, i3) == 0:
                    return np.array([i1, i2, i3])

@njit
def allvals_final5(f, x1, x2, x3, x4, x5):
    for i1 in x1:
        for i2 in x2:
            for i3 in x3:
                for i4 in x4:
                    for i5 in x5:
                        if f(i1, i2, i3, i4, i5) == 0:
                            return np.array([i1, i2, i3, i4, i5])

def compute_values(variables, expr, vals, x):
    free_vars = sorted(expr.free_symbols, key=variables.index)
    f = njit(lambdify(free_vars, expr,
                                      printer=CustomPrinter))

    V = [vals[i] for i in free_vars]
    p = math.prod([len(i) for i in V])
    print("Inputs:", p)

    # a = np.zeros((p, len(V)), dtype=int)
    # for i, val in enumerate(itertools.product(*V)):
    #     a[i] = val


    values = {}

    if x == 'final':
        a = [np.asarray(i) for i in V]
        if len(free_vars) == 3:
            res = allvals_final3(f, *a)
        elif len(free_vars) == 5:
            res = allvals_final5(f, *a)
        else:
            raise ValueError(f"cannot handle final expression with {len(free_vars)} variables")
        values[0] = res
    elif isinstance(expr, Equal):
        a = [np.asarray(i) for i in V]
        if len(free_vars) == 2:
            print("Equal subexpression (2 variables)")
            res = boolallvals2(f, *a)
        elif len(free_vars) == 4:
            print("Equal subexpression (4 variables)")
            res = boolallvals4(f, *a)
        else:
            raise NotImplementedError(f"bool case not implemented for {len(free_vars)} variables")
        for i in range(2):
            if not np.all(res[i] == 0):
                values[i] = res[i]
    else:
        a = cartesian_product(*V)
        res = np.asarray(f(*[a[:, i] for i in range(len(V))]), dtype=int)
        uniq, idxes = np.unique(res, return_index=True)
        for i, idx in enumerate(idxes):
            values[uniq[i]] = a[idx]
    print("Outputs:", len(values))
    return values

def part1_sympy(sympy_z, inputs):
    print("Computing CSE")
    repls, [expr] = cse(sympy_z)
    print(repls)
    print(expr)

    assert len(expr.free_symbols) in {3, 5}, len(expr.free_symbols)

    # for x, subexpr in repls:
    #     if isinstance(subexpr, Equal):
    #         print("bool", len(subexpr.free_symbols))
    #     else:
    #         print("int", len(subexpr.free_symbols))
    # return

    variables = list(inputs)

    values = {}
    vals = {i: np.arange(9, 0, -1) for i in variables}
    for x, subexpr in repls + [('final', expr)]:
        print("Computing subexpression", x)
        values[x] = compute_values(variables, subexpr, vals, x)
        variables.append(x)
        vals[x] = np.asarray(sorted(values[x]))

    breakpoint()
    return values

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
    # inputs = inputs.subs({
    #     # inputs[0]: 9,
    #     # inputs[1]: 9,
    #     # inputs[2]: 9,
    #     # inputs[3]: 9,
    #     # inputs[4]: 9,
    #     # inputs[5]: 9,
    #     # inputs[6]: 9,
    #     # inputs[7]: 9,
    #     # inputs[8]: 9,
    #     # inputs[9]: 9,
    #     # inputs[10]: 9,
    #     # inputs[11]: 9,
    #     # inputs[12]: 9,
    #     # inputs[13]: 9,
    # })
    print("Computing expression")
    sympy_instructions = run_sympy(instructions, inputs)
    expr = sympy_instructions['z']
    # print(expr)
    ans = part1_sympy(expr, inputs)
    print(ans)
    print(''.join([str(i) for i in ans[:14]]))

    # free_inputs = sorted(expr.free_symbols, key=lambda i:
    #                      inputs.index(i))
    # print(free_inputs)
    # ans = part1_sympy(expr, free_inputs)
    # print(ans)
    # res = ''.join([str(i) for i in inputs.subs(ans).subs({i: 9 for i in inputs})])
    # print(res)
    # print(run(instructions, [int(i) for i in res]))
