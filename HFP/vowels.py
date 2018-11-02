#!python

vowels = ['a','e','i','o','u']
word = input("Provide a word")
found = []
for letter in word:
    if letter in vowels:
        if not letter in found:
            found.append(letter)

print (found)
