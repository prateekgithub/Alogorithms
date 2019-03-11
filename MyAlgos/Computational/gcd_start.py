#!/usr/bin/env python3
"""
Computional Algorithm to find GCD of two numbers.

"""

def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t%b

    return a

print(gcd(60,12))
print(gcd(60,100))
