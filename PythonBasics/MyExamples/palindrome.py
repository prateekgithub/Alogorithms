#!/usr/bin/env python3

def main():
    myStr = input('Enter a string: ')
    print('String {} is Palindrome'.format(myStr)) if isPalin(myStr) else print('String {} is not Palindrome'.format(myStr))

def isPalin(myStr):
    if myStr == myStr[::-1]:
        return True
    else:
        return False

if __name__ == '__main__': main()
