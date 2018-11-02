#!python

vowels = ['a','e','i','o','u']
word = "Milliways"
found = []
for letter in word:
    if letter in vowels:
        print(letter)
        if not letter in found:
            found.append(letter)

print (found)
