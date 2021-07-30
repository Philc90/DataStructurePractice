class Heap:
    def __init__(self, max=True):
        self.heapArray = []
        self.isMaxHeap = max

    def insert(self, elem):
        self.heapArray.append(elem)
        self._reHeapify()

    def _reHeapify(self):
        iLast = len(self.heapArray) - 1
        iParent = int((iLast-1)/2)
        while iParent >= 0 and self._shouldSwap(iLast, iParent): # swap with parent
            self.heapArray[iLast], self.heapArray[iParent] = self.heapArray[iParent], self.heapArray[iLast]
            iLast = iParent
            iParent = int((iLast-1)/2) # recompute parent

    def _shouldSwap(self, iLast, iParent):
        if self.isMaxHeap: return self.heapArray[iLast] > self.heapArray[iParent]
        else: return self.heapArray[iLast] < self.heapArray[iParent]

    def __str__(self):
        return str(self.heapArray)

def heapSort(arr):
    heap = Heap(False) # min heap
    sortedArr = []
    for a in arr:
        heap.insert(a)
    while not heap.isEmpty():
        heap.pop(a)

# data = [0,1,4,2,3,5,3]
data = [12,4,5,3,8,7,9,13]

heap = Heap(True)
print('Max Heap Demo:')
for d in data:
    heap.insert(d)
    print(heap)

print('')

heap = Heap(False)
print('Min Heap Demo:')
for d in data:
    heap.insert(d)
    print(heap)

