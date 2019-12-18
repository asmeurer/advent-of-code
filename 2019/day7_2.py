from day7_1 import input

from itertools import permutations

def compute_amplitude(progs):
    in_ = 0
    try:
        while True:
            for p in progs:
                in_ = p.send(in_)
                next(p)
    except StopIteration:
        return in_

def try_permutations(input):
    A = []
    for perm in permutations(range(5, 10)):
        progs = [prog(input) for i in perm]
        for p, i in zip(progs, perm):
            next(p)
            p.send(i)
        A.append((compute_amplitude(progs), perm))

    return max(A)

def prog(l, print_out=True):
    res = list(map(int, l.split(',')))
    out = None
    i = 0
    while True:
        instr, modes = split_op(res[i])
        if instr == '99':
            break

        args = []
        for j, m in enumerate(modes):
            args.append(res[res[i + j + 1]] if m[0] == '0' else res[i + j + 1])
        assert len(args) == n_args[instr]

        if instr == '01':
            res[res[i+3]] = args[0] + args[1]
            i += 4
        elif instr == '02':
            res[res[i+3]] = args[0] * args[1]
            i += 4
        elif instr == '03':
            assert modes[0] == '0'
            res[res[i + 1]] = (yield)
            i += 2
        elif instr == '04':
            out = args[0]
            if print_out:
                yield out
            i += 2
        elif instr == '05':
            if args[0] != 0:
                i = args[1]
            else:
                i += 3
        elif instr == '06':
            if args[0] == 0:
                i = args[1]
            else:
                i += 3
        elif instr == '07':
            res[res[i + 3]] = int(args[0] < args[1])
            i += 4
        elif instr == '08':
            res[res[i + 3]] = int(args[0] == args[1])
            i += 4
        else:
            raise ValueError(i)

n_args = {
    "01": 3,
    "02": 3,
    "03": 1,
    "04": 1,
    "05": 2,
    "06": 2,
    "07": 3,
    "08": 3,
    '99': 0
}

write_instrs = ['01', '02', '07', '08']

def split_op(op):
    op = '00000' + str(op)
    instr = op[-2:]
    modes = op[:-2][::-1]
    modes = modes[:n_args[instr]]

    assert all(i in '01' for i in modes)
    if instr in write_instrs:
        assert modes[-1] != '1'

    return instr, modes

test_input1 = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'

test_input2 = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'

if __name__ == '__main__':
    print("Test 1")
    print("Should give 139629729 (9,8,7,6,5)")
    print(try_permutations(test_input1))

    print("Test 2")
    print("Should give 18216 (9,7,8,5,6)")
    print(try_permutations(test_input2))

    print("Day 7 part 2")
    print(try_permutations(input))
