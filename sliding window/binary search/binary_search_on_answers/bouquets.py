

# flower 1 blooms on day 1
# # flower 2 blooms on day 10 
# flower 3 blooms on day 3
# Flower 4 blooms on day 10
# Flower 5 blooms on day 2

# [1,10,3,10,2] ==> [day1,day2,day3] like that 

# here like each element in the array represent a one flower 

#{VVVVIMP}
#  i.e length of bloomday is len(bloomday) = 5 i.e total no. of flowers avaiable is '5' 

# you need the 'm' bouquets  => mini_days required to make 'm' bouquet's
# each bouquet requires 'k' flowers

#  k = require no. of flowers 
# len(bloomday) = available flowers

#  mid = answer = max_

# optimal solution 

def minimum_days_to_make_m_bouquets(bloomdays,m,k):
    
    n = len(bloomdays)
    if m*k > n:
        return -1
    
    def possible(min_days):               #  How many bouquets can I make using flowers that have bloomed by this day?
        bouquets_possible = 0
        flowers = 0 
        
        for bloom in bloomdays:
            if bloom <= min_days:
                flowers += 1
                if flowers == k:
                    bouquets_possible += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets_possible >= m
    pass


    l = min(bloomdays)      # smallest day that a flower can be bloomed
    r = max(bloomdays)      # largest day that every flower HAS TO BE BLOMMED 
    answer  = r
    while l <= r:
        mid = l + (r-l)//2
        if possible(mid):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
    return answer 
    
    
print(minimum_days_to_make_m_bouquets([1,10,3,10,2],3,1))

