import heapq

def median_in_data_stream(values):
    
    if not values:          # if empty list 
        return None
    
    max_heap = []  # Stores the smaller half (negated for max-heap)
    min_heap = []  # Stores the larger half
    
    for val in values:
        # Step 1: Push to max_heap (invert value for max heap)
        heapq.heappush(max_heap, -val)
        
        largest = - heapq.heappop(max_heap)
        
        heapq.heappush(min_heap,largest)
        
        if len(min_heap) > len(max_heap):
            smallest = heapq.heappop(min_heap)
            heapq.heappush(max_heap,-smallest)
            
    if len(max_heap) > len(min_heap):
        return -max_heap[0]
    return (-max_heap[0] + min_heap[0])/2

values = [2, 3, 4, 5]
print(median_in_data_stream(values))  # Output: 3.5