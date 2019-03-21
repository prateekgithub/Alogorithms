#!/usr/bin/env python3

def quick_sort(dataset, first, last):
    if first < last:
        pivotIdx = partition(dataset, first, last)

        quick_sort(dataset, first, pivotIdx - 1)
        quick_sort(dataset, pivotIdx + 1, last)

def partition(datavalues, first, last):
    # Choose the first item as the pivot value
    pivotValue = datavalues[first]

    # estaiblish upper and lower index
    lower = first + 1
    upper = last

    # start searching for the crossing point
    done = False
    while not done:
        # advance the lower index
        while lower <= upper and datavalues[lower] <= pivotValue:
            lower += 1

        # advance the upper index
        while datavalues[upper] >= pivotValue and upper >= lower:
            upper -= 1

        # if two indexes cross we found the split point
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # when the split point is found, exchange pivotValue with upper index value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return split pointer index
    return upper

def main():
    items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Original: {}".format(items))
    quick_sort(items, 0, len(items)-1)
    print("Result: {}".format(items))

if __name__=='__main__':
    main()
