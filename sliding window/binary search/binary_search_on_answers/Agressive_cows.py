


# optimal solution 

def agressive_cows(stalls,cows):
    stalls.sort()
    def possible(max_distance):
        cows_placed = 1
        last_position = stalls[0]
        for i in range(1,len(stalls)):
            if stalls[i] - last_position >= max_distance:
                cows_placed += 1
                last_position = stalls[i]
        return cows_placed >= cows
    l = 1
    r = max(stalls) - min(stalls)
    answer = r
    while l <= r:
        mid = l +(r-l)//2
        if possible(mid):
            answer = mid 
            l = mid + 1
        else:
            r = mid - 1
    return answer
print(agressive_cows([1, 2, 4, 8, 9],3))            #3

print(agressive_cows( [10, 1, 2, 7, 5],3))          #9