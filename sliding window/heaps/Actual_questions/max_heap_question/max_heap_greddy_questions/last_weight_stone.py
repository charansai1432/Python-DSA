
def lastStoneWeight(stones):
    # BF approach which provides the TC => O(n2 log n )
    while len(stones) > 1 :
        stones.sort(reverse=True)

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
        
    if len(stones) == 0:return 0 

    return -stones[0]
stones = [2,7,4,1,8,1]

print(last_stone_weight(stones))            # 1