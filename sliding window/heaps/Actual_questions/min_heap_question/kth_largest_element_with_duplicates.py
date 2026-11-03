
#  kth largest element with duplicates 

#  pattern is min_heap of size k 

#  same as kth largest element {VVIMP} but here in the array we have the duplicates 

#  imagine if we have the [elements like] -> [8, 8, 5, 3, 10, 10, 7]
#  
#  after inserting into the heap at final heap we have the [8,8,10] and k = 3 

#  then here 1st largest element is 10 
# 2nd largest element is 8 
# and 3rd largest element is 8  

#  {VVVIMP} ==> It simply means if the same number appears multiple times, we count every occurrence separately

#  i.e if same elemet appear's more times ===> we will calucalate it separately like even duplicate is there .. we will consider it as 2nd,3rd,4th largest elements like that.


import heapq

def findKthLargest( nums, k):

    heap = []

    for num in nums:

        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

print(findKthLargest( [8, 8, 5, 3, 10, 10, 7],3))


# Complexity
# - Time: (O(n log k))

# - Space: (O(k))