import math
# Parent node = i
# Left Child = 2*i + 1
# Right Child = 2*i + 2

class MaxHeap:

    def __init__(self):
        self.length = 0
        

    def find_parent(self,index):
        return math.floor((index - 1) / 2)
    
    def left_child(self,index):
        return 2*index + 1
    
    def right_child(self,index):
        return 2*index + 2
    
    def max_heapify(self,arr,n, i):
        self.length = n
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left child
        r = 2 * i + 2  # right child
  
    # Check if left child of root exists and is greater than root
        if l < n and arr[l] > arr[largest]:
            largest = l
  
    # Check if right child of root exists and is greater than root
        if r < n and arr[r] > arr[largest]:
            largest = r
  
    # If largest is not root, swap the root with the largest element
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
  
        # Recursively heapify the affected sub-tree
            self.max_heapify(arr, n, largest)

    def insert(self,heap,element):
        self.length += 1
        heap.append(element)
        index = len(heap) - 1

        while(index > 0):
            parent = self.find_parent(index)
        

            if(heap[index] > heap[parent]):
                temp = heap[parent]
                heap[parent] = heap[index]
                heap[index] = temp

            index = parent
    

    def create_heap(self,arr):
        heap = []
        for num in arr:
            self.insert(heap,num)

        return heap



    def delete(self,heap):
        deleted = heap[0]
        heap[0] = heap[self.length - 1]
        heap[self.length - 1] = deleted

        
        index = 0
        left = self.left_child(index)
        right = self.right_child(index)
        flag = True
        self.length -= 1

        while(flag and left < self.length - 1):
            left_child = heap[left]
            right_child = heap[right]

            nextIndex = None
            swapped = None
            if(left_child > right_child):
                swapped = left_child
                nextIndex = left

            else:
                swapped = right_child
                nextIndex = right

            if(heap[index] < swapped):
                temp = heap[index]
                heap[index] = swapped
                heap[nextIndex] = temp

            else:
                flag = False

        
        #print(heap)
        return deleted


    def heap_sort(self,heap):

        while(self.length > 0):
            self.delete(heap)
    

arr = [10,20,15,30,40]
max_heap = MaxHeap()
for i in range(len(arr) // 2 - 1,-1,-1):
    max_heap.max_heapify(arr,len(arr),i)

max_heap.heap_sort(arr)
print(arr)

