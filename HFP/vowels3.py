#!/usr/bin/env python

vowels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")
found = {}
for letter in word:
    if letter in vowels:
        if not letter in found:
            found[letter] = 1
        else:
            found[letter] += 1

for vowel in found:
    print("Vowel %s appears %s times"%(vowel,found[vowel]))
