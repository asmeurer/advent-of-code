test_input1 = """
noop
addx 3
addx -5
"""

test_input2 = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

input = open('day10_input').read()

def parse_input(data):
    cmds = []
    for line in data.strip().splitlines():
        if line == 'noop':
            cmds.append(None)
        else:
            cmds.append(int(line.split()[1]))
    return cmds

def execute(cmds):
    xvals = [1]
    for cmd in cmds:
        x = xvals[-1]
        if cmd is None:
            xvals.append(x)
        else:
            xvals.extend([x, x + cmd])

    return xvals

def part1(cmds):
    xvals = execute(cmds)
    signal_strengths = [i*xvals[i-1] for i in [20, 60, 100, 140, 180, 220]]
    print(signal_strengths)
    return sum(signal_strengths)

print("Day 10")
print("Part 1")
print("Test input")
test_cmds1 = parse_input(test_input1)
test_cmds2 = parse_input(test_input2)
cmds = parse_input(input)
print(execute(test_cmds1))
test_xvals2 = execute(test_cmds2)
print(test_xvals2)
print(test_xvals2[20-1])
print(test_xvals2[60-1])
print(test_xvals2[100-1])
print(test_xvals2[140-1])
print(test_xvals2[180-1])
print(test_xvals2[220-1])
print(part1(test_cmds2))
print("Puzzle input")
print(part1(cmds))
