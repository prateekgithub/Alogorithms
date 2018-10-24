#!python

def print_recur(n):
  if n == 0:
    return 0
  else:
    print n
    return print_recur(n-1)

print(print_recur(4))
