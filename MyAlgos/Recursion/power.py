#!/usr/bin/env python3

def power_func(num, exp):
    if exp == 0:
        return 1
    else:
        return num*power_func(num,exp - 1)

print(power_func(2,3))
print(power_func(4,3))
