test_input = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

input = open('day07_input').read()

import pprint

def get_filesystem(data):
    root = {'/': {}}
    curdir = root
    inls = False

    for line in data.strip().splitlines():
        if line.startswith('$ cd '):
            inls = False
            dirname = line[len('$ cd '):]
            if dirname == '/':
                curdir = root
            else:
                curdir = curdir[dirname]
        elif line.startswith('$ ls'):
            inls = True
        elif line.startswith('dir '):
            assert inls
            dirname = line[len('dir '):]
            curdir[dirname] = {'..': curdir, '/': {}}
        elif line[0].isdigit():
            assert inls
            size, filename = line.split()
            curdir['/'][filename] = int(size)
        else:
            raise ValueError(f"Unknown line: {line!r}")

    return root

def dirsize(dir):
    return sum(dir['/'].values()) \
        + sum(dirsize(dir[d]) for d in dir if d not in ['/', '..'])

def total_sizes(dir, path=None, sizes=None):
    if not sizes:
        sizes = {'/': dirsize(dir)}
    if not path:
        path = '/'

    for dirname in dir:
        if dirname in ['/', '..']:
            continue
        subdir = dir[dirname]
        path = path + dirname + '/'
        sizes[path] = dirsize(subdir)
        total_sizes(subdir, path, sizes)
    return sizes

def part1(filesystem):
    sizes = total_sizes(filesystem)
    # print(sizes)
    small_sizes = [i for i in sizes if sizes[i] < 100000]
    # print(small_sizes)
    return sum(i for i in sizes.values() if i < 100000)

def part2(filesystem):
    total_space = 70000000
    needed_unused = 30000000
    filesystem_size = dirsize(filesystem)
    unused = total_space - filesystem_size
    difference = needed_unused - unused

    sizes = total_sizes(filesystem)
    for s in sorted(sizes, key=lambda i: sizes[i]):
        if sizes[s] >= difference:
            break

    print(s)
    return sizes[s]

print("Day 7")
print("Part 1")
print("Test input")
test_filesystem = get_filesystem(test_input)
pprint.pprint(test_filesystem)
print(dirsize(test_filesystem['a']['e']))
print(dirsize(test_filesystem['a']))
print(dirsize(test_filesystem['d']))
print(dirsize(test_filesystem))
print("Answer:")
print(part1(test_filesystem))

print("Puzzle input")
filesystem = get_filesystem(input)
# pprint.pprint(filesystem)
print(dirsize(filesystem))
print("Answer:")
print(part1(filesystem))


print("Part 2")
print("Test input")
print(total_sizes(test_filesystem))
print(part2(test_filesystem))
print("Puzzle input")
print(part2(filesystem))
