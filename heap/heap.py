class MaxHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = [0]*capacity
        self.size = 0
        

    def insert(self, value):
        if self.size == self.capacity:
            print("Heap is full")
            return 
    
        self.heap[self.size] = value
        self._swim(self.size)
        self.size+=1

    def _swim(self, index):
        while index>0 and self.heap[index] > self.heap[self.parentIndex(index)]:
            self._swap(index, self.parentIndex(index))

    def deleteMax(self):
        if self.size == 0:
            return "heap is empty"
        maxV = self.heap[0]
        self._swap(0,self.size-1)
        self.size -=1
        self.heapify(0)
        return maxV
    
    def heapify(self, index):
        largest = index 
        left = 2*index
        right = 2*index + 1
        if left < self.size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right 

        if largest != index:
            self._swap(index, largest)
            self.heapify(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heap_sort(self):
        original_size = self.size 
        for i in range(self.size-1,0 ,-1):
            self.__swap(0,i)
            self.size -= 1
            self.heapify(0)
        self.size = original_size





def getLeftChild(idx):
    return 2*idx
def getRightChild(idx):
    return 2*idx +1
def parentIndex(idx):
    if idx == 1:
        return None 
    else:
        return idx // 2 
    
def max_heapify(A, index, heap_size): # Also known as "Sink"
    """
    Ensures the max-heap property is maintained by sinking
    the element at `index` down the heap. Also known as "Sink".
    Compares the element at `index` with its left and right children, and
    swaps it with the largest of the three,
    recursively heapifying the affected subtree.
    """

    left_child_index = getLeftChild(index)
    right_child_index = getRightChild(index)

    # Finding the largest among index (parent), left child, and right child
    largest = index # parent

    if (left_child_index <= heap_size) and (left_child_index > 0):
        if A[left_child_index] > A[largest]:
            largest = left_child_index

    if (right_child_index <= heap_size) and (right_child_index > 0):
        if A[right_child_index] > A[largest]:
            largest = right_child_index

    # If index is not the largest, swap it with the left/right child which is largest
    if largest != index:

        # Swapping A[index] and A[largest]
        temp = A[index]
        A[index] = A[largest]
        A[largest] = temp

        # Recursively heapify the affected subtree (child)
        max_heapify(A, largest, heap_size)

def get_heap_size(heap):
    count = 0
    for i in range(1, len(heap)):
        if heap[i]:
            count +=1

    return count
def build_max_heap(A):
    heap_size = get_heap_size(A)
    for i in range(heap_size//2, 0, -1):
        max_heapify(A, i , heap_size)


def heapIncreaseKey(heap, idx, key):
    if key < heap[idx]:
        print("Key is similar")
        return 
    heap[idx] = key 
    while idx > 1 and heap[parentIndex(idx)] < heap[idx]:
        temp = heap[parentIndex(idx)]
        heap[parentIndex(idx)] = heap[idx]
        heap[idx] = temp
        idx = parentIndex[idx]