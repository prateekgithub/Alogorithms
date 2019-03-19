#!/usr/bin/env python3

def bubbleSort(myList):
    # Start with the list length and decrement each time as list length 
    for j in range(len(myList) - 1, 0, -1):
        for i in range(j):
            if myList[i] > myList[i+1]:
                myList[i],myList[i+1] = myList[i+1],myList[i]
        print("Current state: {}".format(myList))

def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print("Result: {}".format(list1))

if __name__=='__main__':
    main()
