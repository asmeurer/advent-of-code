from day23_1 import prog, defaultlist

def run(input):
    ins = [defaultlist() for i in range(50)]
    progs = [prog(input, in_) for i, in_ in enumerate(ins)]
    for i, in_ in enumerate(ins):
        in_.append(i)
    nat = ()
    natys = set()
    idle = {i: False for i in range(50)}
    while True:
        for i, p in enumerate(progs):
            addr = next(p)
            if addr == None:
                idle[i] = True
                if all(idle.values()) and nat:
                    print("all idle, sending", nat)
                    ins[0].extend(nat)
                    if nat[1] in natys:
                        return nat[1]
                    natys.add(nat[1])
                    break
                continue
            idle[i] = False
            x = next(p)
            y = next(p)
            print(i, addr, x, y)
            if addr == 255:
                nat = [x, y]
            else:
                ins[addr].extend([x, y])

with open('day23-input') as f:
    input = f.read()

def main():
    print("Day 23 part 2")
    print(run(input))

if __name__ == '__main__':
    main()
