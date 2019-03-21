#!/usr/bin/env python3

def rem_trail_0(myNum):
    return (int(str(myNum).rstrip('0')))

def main():
    print(rem_trail_0(12340000))

if __name__ == '__main__': main()
