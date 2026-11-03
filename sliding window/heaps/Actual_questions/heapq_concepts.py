# practising the basic heapq in-built functions

# heappush,heapify,heappop


###### heapq which default use's the min_heap in it #########
## if we want to use the heapq as max_heap ### we have to multiply the every with '-' minus symbol 

import heapq
heap = [2,1,4,5,9]
heapq.heapify(heap)         # heapify which converts the every list into the min_heap 
print(heap)

heapq.heappush(heap,0)          # even after inserting a new element it maintain the min_heap property 
print(heap)

smallest = heapq.heappop(heap)      # same for the pop operation --> even after poping heappop maintain's the min_heap property         
print(smallest)

print(heap[0])          # in the min_heap the smalllest element lies at the index position right 



### using the heapq --> to generate the max_heap 

print("max_heap down here operations")

heap = [-10,-20,-30,-40]

heapq.heappush(heap,-50)                # which returns the min_heap property by default ... but with the -ve symbol it became the max_heap 

print(heap)

largest = -heapq.heappop(heap)
print(largest)

print(heap)                             # remember the max_element alway's there at the root ... same as min_heap above operations okk


largest_element = -heap[0]
print(largest_element)


