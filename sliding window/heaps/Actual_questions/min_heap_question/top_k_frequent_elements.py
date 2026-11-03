
# the top k frequent elements in an array is a pattern of heap + hashmap 

# top k elements --> i.e we have to main tain a window of k when it exceeds k we will pop the smallest element 

#  frequent --> we have to use the hash map when to know the how many times a number is repeated 

#  question is ===> we want the 'k' most frequent element's in an array 


#  pattern is hashmap + min_heap 

def top_k_frequent_elements(nums,k):
    
    from collections import Counter 
    freq = Counter(nums)
    print(freq)
    heap = []
    import heapq
    for num in freq:
        heapq.heappush(heap,(freq[num],num))
        
        if len(heap)>k:
            heapq.heappop(heap)
            
    result = []
    while heap:
        freq , num = heapq.heappop(heap)
        result.append(num)
    return result
nums = [1,1,1,2,2,3,4,]
print(top_k_frequent_elements(nums,2))