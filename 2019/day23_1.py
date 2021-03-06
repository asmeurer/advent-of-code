from collections import defaultdict

from day13 import split_op, write_instrs, n_args

def prog(l, in_):
    res = defaultdict(int, enumerate(map(int, l.split(','))))
    out = None
    i = 0 # instruction counter
    r = 0 # relative base
    iterations = 0

    while True:
        iterations += 1
        # print("Iteration:", iterations)
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
            res[addr] = in_.pop(0)
            if res[addr] == -1:
                yield
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

class defaultlist(list):
    def pop(self, index):
        try:
            return super().pop(index)
        except IndexError:
            return -1

def run(input):
    ins = [defaultlist() for i in range(50)]
    progs = [prog(input, in_) for i, in_ in enumerate(ins)]
    for i, in_ in enumerate(ins):
        in_.append(i)
    while True:
        for i, p in enumerate(progs):
            addr = next(p)
            if addr == None:
                continue
            x = next(p)
            y = next(p)
            print(i, addr, x, y)
            if addr == 255:
                return y
            ins[addr].extend([x, y])

with open('day23-input') as f:
    input = f.read()

def main():
    print("Day 23 part 1")
    print(run(input))

if __name__ == '__main__':
    main()
