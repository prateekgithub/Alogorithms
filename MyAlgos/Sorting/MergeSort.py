#!/usr/bin/env python3

def merge_sort(dataset):
    """
    First break the dataset into single elements
    and then start merge them in ascending order
    """
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # recursively break down dataset
        merge_sort(leftarr)
        merge_sort(rightarr)

        # Start merging dataset once divided into individual elements
        i = 0
        j = 0
        k = 0

        # while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # if leftarr still has values
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # if rightarr still has values
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1

def main():
    items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Original: {}".format(items))
    merge_sort(items)
    print("Result: {}".format(items))

if __name__=='__main__':
    main()
