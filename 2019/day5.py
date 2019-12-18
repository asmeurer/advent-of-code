def prog(l, in_):
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
            res[res[i + 1]] = in_.pop(0)
            i += 2
        elif instr == '04':
            out = args[0]
            print(out)
            i += 2
        elif instr == '05':
            if args[0] != 0:
                res[res[i]] = args[1]
            else:
                i += 3
        elif instr == '06':
            if args[0] == 0:
                res[res[i]] = args[1]
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

    return out

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

input = '3,225,1,225,6,6,1100,1,238,225,104,0,1101,40,71,224,1001,224,-111,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1102,66,6,225,1102,22,54,225,1,65,35,224,1001,224,-86,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1102,20,80,225,101,92,148,224,101,-162,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1102,63,60,225,1101,32,48,225,2,173,95,224,1001,224,-448,224,4,224,102,8,223,223,1001,224,4,224,1,224,223,223,1001,91,16,224,101,-79,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1101,13,29,225,1101,71,70,225,1002,39,56,224,1001,224,-1232,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,14,59,225,102,38,143,224,1001,224,-494,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1102,30,28,224,1001,224,-840,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,677,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,344,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1007,677,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,389,101,1,223,223,1008,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,108,677,226,224,1002,223,2,223,1006,224,419,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,434,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,449,101,1,223,223,7,677,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,1007,226,226,224,1002,223,2,223,1005,224,509,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,524,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,539,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,554,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,569,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,584,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,599,101,1,223,223,1008,677,677,224,1002,223,2,223,1005,224,614,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,629,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,644,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,1107,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226'

if __name__ == '__main__':
    print("Part 1")
    prog(input, [1])

    print("Part 2")
    print("Test 1")
    test1 = "3,9,8,9,10,9,4,9,99,-1,8" # == 8
    print("Should output 1")
    prog(test1, [8])
    print("Should output 0")
    prog(test1, [9])
    print("Test 2")
    test2 = "3,9,7,9,10,9,4,9,99,-1,8" # < 8
    print("Should output 1")
    prog(test2, [7])
    print("Should output 0")
    prog(test2, [9])
    print("Test 3")
    test3 = "3,3,1108,-1,8,3,4,3,99" # == 8
    print("Should output 1")
    prog(test3, [8])
    print("Should output 0")
    prog(test3, [9])
    print("Test 4")
    test4 = "3,3,1107,-1,8,3,4,3,99" # < 8
    print("Should output 1")
    prog(test4, [7])
    print("Should output 0")
    prog(test4, [9])

    print("Test 5")
    test5 = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9" # != 0
    print("Should output 1")
    prog(test5, [1])
    print("Should output 0")
    prog(test5, [0])

    print("Test 6")
    test6 = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1" # != 0
    print("Should output 1")
    prog(test6, [1])
    print("Should output 0")
    prog(test6, [0])

    print("Test 7")
    # < 8 -> 999
    # == 8 -> 1000
    # > 8 -> 1001
    test7 = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    print("Should output 999")
    prog(test7, [7])
    print("Should output 1000")
    prog(test7, [8])
    print("Should output 1001")
    prog(test7, [9])
