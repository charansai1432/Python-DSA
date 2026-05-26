
# brute force approach 

def koko_eating_bananas(piles,h):
    import math 
    
    max_speed = max(piles)
    for speed in range(1,max_speed+1):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile/speed)
        if total_hours <= h:
            return speed
print(koko_eating_bananas([3,6,7,11],8))            #4



# optimal solution approach 
import math
def koko_eating_bananas(piles,h):
    
    def possible(speed):            # fesability function 
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/speed)
        return hours <= h
    
    
    l =  1
    r = max(piles)
    
    ans = r
    while l <= r:
        mid = l + (r-l)//2
        if possible(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans
print(koko_eating_bananas([3,6,7,11],8))        #4

# The time complexity is tc = >  O(nlog(max(piles)))

