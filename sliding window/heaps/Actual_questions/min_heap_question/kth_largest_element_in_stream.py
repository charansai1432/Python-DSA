# 1. Understand the problem
# You are given:
# - An integer k.
# - An initial array of numbers.
# - A stream of new numbers arriving one by one.
# After every new number is added, return the Kth largest element.


# question is .. we have to return k largest element in an array ---> and also when a new element is added to the array for that array .. we have to find the kth largest element in the array 

# pattern is {{VVVIMP}
# min_heap
# }

# Why Min Heap of size K? ==> we need to maintain the 'k' elements in the heap .. min_heap which helps us to remove all the smallest elements in the heap 
#  such that after removing all the smallest elements --> we remain with the largest elements in the heap


# {VVVIMP}

# Whenever a new number arrives:
# 1. Insert it into the heap.
# 2. If heap size exceeds K, remove the smallest.
# 3. Return the root.


import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heap = []
        self.k = k

    
        for num in nums:
            heapq.heappush(self.heap,num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
    
nums = [1,2,3,4,4]
val = 4
k = 3
# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(k, nums)
param_1 = obj.add(val)
