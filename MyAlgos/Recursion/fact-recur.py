#!python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

n = input("Enter number to get factorial of: ")
print (factorial(n))
