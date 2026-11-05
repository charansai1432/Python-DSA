
ropes = [4,3,2,6]
# BF approach 
def minimum_cost_of_rope(ropes):
    min_cost = 0
    while len(ropes) > 1 :
        first_small = min(ropes)
        ropes.remove(first_small)
         
        second_small = min(ropes)
        ropes.remove(second_small)
        
        min_cost += first_small + second_small
        
        new_rope = first_small + second_small 
        
        ropes.append(new_rope)
    return min_cost
print(minimum_cost_of_rope(ropes))



# Repeatedly combine the two smallest elements + add each combination cost + reinsert the result = Huffman-style Greedy + Min Heap pattern.

# optimal solution------ min_heap + greddy

ropes = [4, 3, 2, 6]
# ropes = [5, 2, 4, 3]
def minimum_cost_of_ropes(ropes):
    import heapq
    min_cost = 0
    heapq.heapify(ropes) 
    
    while len(ropes) > 1:
        first_small = heapq.heappop(ropes)
        second_small = heapq.heappop(ropes)
        
        new_rope = first_small + second_small 
        
        min_cost += first_small + second_small
        
        heapq.heappush(ropes,new_rope)
    return min_cost
print(minimum_cost_of_ropes(ropes))        