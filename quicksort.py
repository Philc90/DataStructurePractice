# implementation of quicksort from CLRS. Uses last index as pivot

def quicksort(array):
    quicksortHelper(array, 0, len(array) - 1)

def quicksortHelper(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quicksortHelper(array, start, pivot - 1)
        quicksortHelper(array, pivot + 1, end)

def partition(array, start, end):
    pivotVal = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= pivotVal:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[end] = array[end], array[i+1]
    return i + 1

test = [2,10,5,1,3,9,44,-1,3]
quicksort(test)
print(test)