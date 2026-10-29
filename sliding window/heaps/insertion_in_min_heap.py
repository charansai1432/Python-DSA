
heap = [4, 7, 6, 12, 9]
def insertion_in_minheap(heap,val):
    
    heap.append(val)
    
    i = len(heap) - 1 
    
    while i > 0:
        
        parent = (i-1)//2
        
        if heap[parent] <= heap[i]:
            break 
        
        elif heap[parent] >= heap[i]:
            heap[parent],heap[i] = heap[i],heap[parent]
            
        i = parent 
    
    return heap 
print(insertion_in_minheap(heap,2))
    
    
    