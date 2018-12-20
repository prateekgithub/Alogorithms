#!python

def print_recur(n):
  if n == 0:
    return 0
  else:
    print n
    return print_recur(n-1)

n = input("Enter length of recursion: ")
print(print_recur(n))
