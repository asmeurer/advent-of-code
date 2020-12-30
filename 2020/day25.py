test_input = (5764801, 17807724)
input = (3418282, 8719412)

x = 7
p = 20201227

def compute_private_key(public_keys):
    key1, key2 = public_keys
    loop1 = discrete_log(p, key1, x)
    loop2 = discrete_log(p, key2, x)
    res = pow(key1, loop2, p)
    assert res == pow(key2, loop1, p)
    return res

from sympy import discrete_log

print("Day 25")
print("Part 1")
print("Test input")
print(compute_private_key(test_input))

print("Puzzle input")
print(compute_private_key(input))
