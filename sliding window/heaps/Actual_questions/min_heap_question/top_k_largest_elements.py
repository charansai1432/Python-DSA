 
 
#   just return the top 3 largest element ==> min_heap 
 
 
def top_k_largest_element(nums,k):
    
    heap = []
    import heapq
    
    for num in nums:
        heapq.heappush(heap,num)
        
        if len(heap) > k:
            heapq.heappop(heap)
            
    return heap  


nums = [3, 2, 1, 5, 6, 4]
k = 3
print(top_k_largest_element(nums,k))