#!/usr/bin/env python3

def duplicateChar(myStr):
    strChar = {}
    for i in myStr:
        if i in strChar:
            strChar[i] += 1
        else:
            strChar[i] = 1
    return strChar

print(duplicateChar("hello"))
