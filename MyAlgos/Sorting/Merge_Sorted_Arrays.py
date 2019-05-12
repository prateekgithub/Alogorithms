#!python3

arr1 = [2,5,7,9]
arr2 = [1,3,6,8]
arr = []

i = 0
j = 0
k = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        arr.append(arr1[i])
        i += 1
    else:
        arr.append(arr2[j])
        j += 1
    k += 1

while i < len(arr1):
    arr.append(arr1[i])
    k += 1
    i += 1

while j < len(arr2):
    arr.append(arr2[j])
    k += 1
    j += 1

print(arr)
