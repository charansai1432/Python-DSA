
# this is the question we have to find the koko(monkey) eating bananas => find the minimum speed of the koko that requires to complete the entire pile 

#  Here we have to find the minimum speed of koko to complete the entire pile 

### Here the actual question is the koko has to complete all piles in the given time in which minimum speed the koko has to eat to complete all piles in that given time only

# that here we have to find the minimum speed koko to complete all piles <= time is given in the question 

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
        
        hours = 0                           # the initial time , hours = 0 i.e that koko hasn't started eating at all 
        
        for pile in piles:
            hours += math.ceil(pile/speed)          # this is the simple physics formula like => speed = distance/time ===> Time = distance/speed
            
        return hours <= h
    
    
    l =  1                          # the koko can able to eat at speed = 1 
    r = max(piles)                          #the koko can able to eat the all piles in this max_speed = r = max(piles) 
                                # in the previous question l = max() ==> here only r = max() => which gives the koko can able to complete all piles at this speed
    ans = r                             # here this provides the answer from the max_speed to minimum_spped(asked in the question)
    while l <= r:
        mid = l + (r-l)//2
        if possible(mid):
            ans = mid
            r = mid - 1                 # the minimum speed that a koko can eat all piles in the minimum_speed
        else:
            l = mid + 1
    return ans

print(koko_eating_bananas([3,6,7,11],8))        #4

# The time complexity is tc = >  O(nlog(max(piles)))

