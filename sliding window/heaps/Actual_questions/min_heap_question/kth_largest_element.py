# kth largest element --> which we use's the min_heap property 

# we dont need to sort the array in the reverse order and returning the k -1 position which makes time complexity into the o(n log n)
#  here we dont want to sort the every element in the nums array

# we can use the min_heap property 
# 
#  and we will insert the every element in the heap by traverssing the num array 
# 
#  when the heap array exceed the size 'k' --> we will remove the smallest element till the heap array --> using the heapq.heappop(heap)
# at last we only have with the k element's in the heap ... for example [5,6] --> min_heap 5->6 (parent<= children)
                    
                        # here the root itself is the kth largest element 
#

def kth_largest_ele(nums,k):
    
    nums.sort(reverse= True)
    return nums[k-1]

nums = [3,2,1,5,6,4]
k = 2
print(kth_largest_ele(nums,k))



# optimal solutioin 
def kth_largest_element(nums,k):
    
    heap = []
    import heapq
    
    for num in nums:
        heapq.heappush(heap,num)
        
        if len(heap) > k:
            heapq.heappop(heap)
            
    return heap                # where the kth largest element finds ... in the min_heap its the root 

nums = [3, 2, 1, 5, 6, 4]
k = 3
print(kth_largest_element(nums,k))