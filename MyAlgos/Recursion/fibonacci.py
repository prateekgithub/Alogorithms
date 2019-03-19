#!/usr/bin/env python3

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return (fibonacci(num-1)+fibonacci(num-2))

num = int(input("Enter an interger: "))
for i in range(num):
    print(fibonacci(i+1))
