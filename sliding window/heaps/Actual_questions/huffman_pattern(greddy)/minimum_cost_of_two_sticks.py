
sticks = [1, 3, 5, 7]

def minimum_cost_of_two_sticks(sticks):
    import heapq 
    heapq.heapify(sticks)
    min_cost = 0 
    while len(sticks) > 1:
        
        first_smallest=heapq.heappop(sticks)
        second_smallest = heapq.heappop(sticks)
        
        min_cost += first_smallest + second_smallest
        
        new_stick = first_smallest + second_smallest
        
        heapq.heappush(sticks,new_stick)
    return min_cost
print(minimum_cost_of_two_sticks(sticks))

