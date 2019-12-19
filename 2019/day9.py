from collections import defaultdict

def compute_prog(prog, in_=(), print_=False):
    in_ = list(in_)
    out = []
    stop = False
    if in_:
        next(prog)
    while not stop:
        if in_:
            o = prog.send(in_.pop(0))
            if o is not None:
                out.append(o)
                if print_:
                    print(o)
        try:
            o = next(prog)
            if o is not None:
                out.append(o)
                if print_:
                    print(o)
        except StopIteration:
            stop = True
    return out

def prog(l):
    res = defaultdict(int, enumerate(map(int, l.split(','))))
    out = None
    i = 0 # instruction counter
    r = 0 # relative base

    while True:
        instr, modes = split_op(res[i])
        if instr == '99': # Halt
            break

        args = []
        for j, m in enumerate(modes):
            if m[0] == '0':
                args.append(res[res[i + j + 1]])
            elif m[0] == '1':
                args.append(res[i + j + 1])
            elif m[0] == '2':
                args.append(res[res[i + j + 1] + r])
            else:
                raise ValueError("Unrecognized mode %s" % m[0])
        if instr in write_instrs:
            addr = res[i + n_args[instr]]
            if modes[-1] == '2':
                addr += r

        assert len(args) == n_args[instr], (instr, args)

        if instr == '01': # Add
            res[addr] = args[0] + args[1]
            i += 4
        elif instr == '02': # Mul
            res[addr] = args[0] * args[1]
            i += 4
        elif instr == '03': # Input
            res[addr] = (yield)
            i += 2
        elif instr == '04': # Output
            out = args[0]
            yield out
            i += 2
        elif instr == '05': # Jump if nonzero
            if args[0] != 0:
                i = args[1]
            else:
                i += 3
        elif instr == '06': # Jump if zero
            if args[0] == 0:
                i = args[1]
            else:
                i += 3
        elif instr == '07': # Less than
            res[addr] = int(args[0] < args[1])
            i += 4
        elif instr == '08': # Equals
            res[addr] = int(args[0] == args[1])
            i += 4
        elif instr == '09': # Adjust relative base
            r += args[0]
            i += 2
        else:
            raise ValueError("bad instruction %s" % i)

n_args = {
    "01": 3,
    "02": 3,
    "03": 1,
    "04": 1,
    "05": 2,
    "06": 2,
    "07": 3,
    "08": 3,
    "09": 1,
    "99": 0,
}

write_instrs = ['01', '02', '03', '07', '08']

def split_op(op):
    op = '00000' + str(op)
    instr = op[-2:]
    modes = op[:-2][::-1]
    modes = modes[:n_args[instr]]

    assert all(i in '012' for i in modes), modes
    if instr in write_instrs:
        assert modes[-1] != '1', modes
        if modes[-1] == '2':
            pass

    return instr, modes

test_input1 = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
test_input2 = '1102,34915192,34915192,7,4,7,99,0 '
test_input3 = '104,1125899906842624,99'

input = '1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,3,1,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,1,0,1020,1101,0,23,1010,1102,1,31,1009,1101,34,0,1019,1102,38,1,1004,1101,29,0,1017,1102,1,25,1018,1102,20,1,1005,1102,1,24,1008,1101,897,0,1024,1101,0,28,1016,1101,1,0,1021,1101,0,879,1028,1102,1,35,1012,1101,0,36,1015,1101,311,0,1026,1102,1,37,1011,1101,26,0,1014,1101,21,0,1006,1102,1,32,1002,1102,1,33,1003,1102,27,1,1001,1102,1,667,1022,1101,0,892,1025,1101,664,0,1023,1101,30,0,1000,1101,304,0,1027,1101,22,0,1013,1102,1,874,1029,1102,1,39,1007,109,12,21108,40,41,1,1005,1013,201,1001,64,1,64,1106,0,203,4,187,1002,64,2,64,109,5,1205,4,221,4,209,1001,64,1,64,1106,0,221,1002,64,2,64,109,5,21108,41,41,-5,1005,1017,243,4,227,1001,64,1,64,1106,0,243,1002,64,2,64,109,-30,2101,0,8,63,1008,63,30,63,1005,63,269,4,249,1001,64,1,64,1105,1,269,1002,64,2,64,109,15,2101,0,-5,63,1008,63,35,63,1005,63,293,1001,64,1,64,1106,0,295,4,275,1002,64,2,64,109,28,2106,0,-8,1001,64,1,64,1105,1,313,4,301,1002,64,2,64,109,-22,1205,7,329,1001,64,1,64,1106,0,331,4,319,1002,64,2,64,109,-12,1208,6,37,63,1005,63,351,1001,64,1,64,1106,0,353,4,337,1002,64,2,64,109,-3,2108,21,8,63,1005,63,375,4,359,1001,64,1,64,1106,0,375,1002,64,2,64,109,14,1201,-5,0,63,1008,63,39,63,1005,63,401,4,381,1001,64,1,64,1105,1,401,1002,64,2,64,109,17,1206,-9,419,4,407,1001,64,1,64,1105,1,419,1002,64,2,64,109,-10,21101,42,0,-4,1008,1015,42,63,1005,63,445,4,425,1001,64,1,64,1105,1,445,1002,64,2,64,109,-5,1206,7,457,1105,1,463,4,451,1001,64,1,64,1002,64,2,64,109,-6,2107,34,-5,63,1005,63,479,1105,1,485,4,469,1001,64,1,64,1002,64,2,64,109,-8,2102,1,5,63,1008,63,23,63,1005,63,505,1106,0,511,4,491,1001,64,1,64,1002,64,2,64,109,5,2102,1,1,63,1008,63,21,63,1005,63,537,4,517,1001,64,1,64,1105,1,537,1002,64,2,64,109,15,21107,43,44,-6,1005,1014,555,4,543,1106,0,559,1001,64,1,64,1002,64,2,64,109,-6,1207,-7,38,63,1005,63,579,1001,64,1,64,1106,0,581,4,565,1002,64,2,64,109,-17,1201,4,0,63,1008,63,28,63,1005,63,601,1106,0,607,4,587,1001,64,1,64,1002,64,2,64,109,14,2107,31,-9,63,1005,63,625,4,613,1105,1,629,1001,64,1,64,1002,64,2,64,109,15,21102,44,1,-7,1008,1019,44,63,1005,63,651,4,635,1106,0,655,1001,64,1,64,1002,64,2,64,109,3,2105,1,-6,1106,0,673,4,661,1001,64,1,64,1002,64,2,64,109,-14,21101,45,0,2,1008,1017,42,63,1005,63,693,1105,1,699,4,679,1001,64,1,64,1002,64,2,64,109,5,21107,46,45,-8,1005,1012,719,1001,64,1,64,1105,1,721,4,705,1002,64,2,64,109,-19,2108,21,7,63,1005,63,737,1106,0,743,4,727,1001,64,1,64,1002,64,2,64,109,9,1207,-2,25,63,1005,63,761,4,749,1106,0,765,1001,64,1,64,1002,64,2,64,109,-10,1208,1,27,63,1005,63,783,4,771,1106,0,787,1001,64,1,64,1002,64,2,64,109,5,1202,4,1,63,1008,63,29,63,1005,63,807,1106,0,813,4,793,1001,64,1,64,1002,64,2,64,109,8,21102,47,1,0,1008,1013,50,63,1005,63,833,1106,0,839,4,819,1001,64,1,64,1002,64,2,64,109,-12,1202,8,1,63,1008,63,31,63,1005,63,865,4,845,1001,64,1,64,1105,1,865,1002,64,2,64,109,34,2106,0,-7,4,871,1105,1,883,1001,64,1,64,1002,64,2,64,109,-18,2105,1,7,4,889,1105,1,901,1001,64,1,64,4,64,99,21101,0,27,1,21101,915,0,0,1106,0,922,21201,1,13801,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21102,942,1,0,1106,0,922,21201,1,0,-1,21201,-2,-3,1,21102,957,1,0,1105,1,922,22201,1,-1,-2,1106,0,968,21202,-2,1,-2,109,-3,2106,0,0'

if __name__ == '__main__':
    print("Test 1, should output", test_input1)
    print(compute_prog(prog(test_input1)))

    print("Test 2, should output a 16 digit number")
    out = compute_prog(prog(test_input2))
    print(out)
    print(len(str(out[0])), "digits")

    print("Test3, should output 1125899906842624")
    print(compute_prog(prog(test_input3)))

    print("Day 9 part 1")
    print(compute_prog(prog(input), [1]))

    print("Day 9 part 2")
    print(compute_prog(prog(input), [2]))
