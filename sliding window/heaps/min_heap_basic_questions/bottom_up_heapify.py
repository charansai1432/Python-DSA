


# this is a question we are going to build the heap using the min_heap property 
# for that 1st we have to caluclate the last_non_leaf_node and after that we will move backward direction 
# from the last_non_leaf_node(index) to backward till the root node we will move 
# for each index we will check whether that element to it's children valid's the min_heap property or not 


def bottom_up_heapify(heap):
    last_non_leaf_node = (len(heap)//2) - 1
    n = len(heap)
    for i in range(last_non_leaf_node,-1,-1):
        
        while True:
            left = 2*i + 1
            right = 2*i + 2 
            smallest = i 
            if left < n and heap[left] < heap[smallest]:
                smallest = left 
            if right < n and heap[right] < heap[smallest]:
                smallest = right 
            if i == smallest:
                break 
            heap[i],heap[smallest] = heap[smallest],heap[i]
            i = smallest
    return heap 
heap = [8,5,6,2,3]
print(bottom_up_heapify(heap))
