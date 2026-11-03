



#  we are going to return the kth smallest element using the max_heap of size k 

# BF approach 

nums = [7, 10, 4, 3, 20, 15]

def kth_smallest_ele(nums,k):
    nums.sort()                         # sorting in the ascending order 
    return nums[k-1]
print(kth_smallest_ele(nums,3))



# optimal approach 

nums = [7, 10, 4, 3, 20, 15]

def kth_smallest_element(nums,k):
    import heapq 
    heap = []
    for num in nums:
        heapq.heappush(heap,-num)               # '-' which tells us we are performing the max_heap 
        
        if len(heap) > k:
            heapq.heappop(heap)
                                        # [3, 4, 7] --> 3rd smallest element is 7 right 
    
    return -heap[0]                             # at this position in the max_heap we have the maximum value right like parent >= child 
                                    # that position only we will have the kth smallest element --> 3rd smallest element 
                                    
                                    #  for example in the heap we have [3,7,4] ==> after applying the max_heap it became the [7,3,4] so 7 is at root and also if we see clearly 7 is the 3rd smallest element right .... 1st smallest element is 3 and 2nd smallest element is 4 and 3rd smallest element is 7 (asked in the question ) and also 7 is the root so we simply return the root i.e index positon('0') ==> heap[0]
print(kth_smallest_element(nums,3))  # 7 