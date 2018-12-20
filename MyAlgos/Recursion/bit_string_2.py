#!python
import itertools

def bit_strings(n):
    if n == 0: return []
    if n == 1: return ["0", "1"]
    return[digit + bitString for digit in bit_strings(1)
        for bitString in bit_strings(n-1)]

def bit_strings_iter(n):
    return ["".join(seq) for seq in itertools.product("01", repeat=n)]


n = input("Enter length of binary string: ")
print(bit_strings_iter(n))
