# 
# the last stone weight is a question ===> we have to find the weight of last stone in the array 
#  in the question they have mentioned like the ===> we have subtract the two largest stones at every step 
# 
# if the two stones have the same weight we have to destroy it ==> i.e in code we simple use the  continue statement -> which simple lefts teh current iteration and go with the next iteration.
# 
# if two stones are of different weight we simple subtract it and insert to the stone list 
#  
# here at last we only remain with the 1 stone in the heap array or normal so we will return it .
# 
#  at last iteration while len(stones) > 1 i.e we remain with the 1 stone right at that time we dont have any other stone to compare we will break from the while loop.
# 

#           {VVVIMP}  --> max_heap + greddy 
#  max_heap which gives the largest stones every time effectively 
#  greddy --> which repeateadly choose the two largest stone every time --> to lead the optimal answer 
# 
#       if len(stones) == 0 --> means ==>  Suppose the two largest stones have equal weights every time.
#           here in the array have the equal weight every time such case ... stones will become empty --> then len(stones) == 0 means return 0 
# 
def lastStoneWeight(stones):
    # BF approach which provides the TC => O(n2 log n )
    while len(stones) > 1 :
        stones.sort(reverse=True)           # we sort the array ... such that at index '0' position which gives the big element right 

        first = stones.pop(0)
        second = stones.pop(0)

        if first == second:
            continue 
        stone_weight = first - second 
        stones.append(stone_weight)

    if len(stones) == 0:return 0 
    return stones[0]
stones = [2,7,4,1,8,1]      # 1
print(lastStoneWeight(stones))

        # optimal solution approach 
                        # tc => O(n log k )
def last_stone_weight(stones):
    
    import heapq 
        
    for i in range(len(stones)):
        stones[i] = -stones[i]

    heapq.heapify(stones)

    while len(stones) > 1:
        first_stone = -heapq.heappop(stones)
        second_stone = -heapq.heappop(stones)
        stone = first_stone - second_stone

        if first_stone == second_stone:
            continue 
            
        heapq.heappush(stones,-(stone))
        
    if len(stones) == 0:return 0                # Suppose the two largest stones have equal weights every time.

    return -stones[0]
stones = [2,7,4,1,8,1]

print(last_stone_weight(stones))            # 1



def last_stone_weigh(stones):
    import heapq 
    
    max_heap = []
    for stone in stones:
        heapq.heappush(max_heap,-stone)
    heapq.heapify(max_heap)
    while len(max_heap) > 1:
        first_heavy_weight = -heapq.heappop(max_heap)
        second_heavy_weight = -heapq.heappop(max_heap)
        
        if first_heavy_weight == second_heavy_weight:
            continue
        new_stone = first_heavy_weight - second_heavy_weight
        heapq.heappush(max_heap,-new_stone)
    if len(max_heap) == 0:return 0 
    return -max_heap[0]
print(last_stone_weigh(stones=[2,7,4,1,8,1]))