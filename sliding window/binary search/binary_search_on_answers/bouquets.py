

# flower 1 blooms on day 1
# # flower 2 blooms on day 10 
# flower 3 blooms on day 3
# Flower 4 blooms on day 10
# Flower 5 blooms on day 2
# here the index represent the flower and value represent the days
# [1,10,3,10,2] ==> [day1,day2,day3] like that 

# here like each element in the array represent a one flower 

#{VVVVIMP}
#  i.e length of bloomday is len(bloomday) = 5 i.e total no. of flowers avaiable is '5' 

# you need the 'm' bouquets  => mini_days required to make 'm' bouquet's
# each bouquet requires 'k' flowers

#  k = require no. of flowers 
# len(bloomday) = available flowers

#  mid = answer = max_

# here the search space could be from the l to r i.e ====> days from L to R like day-1 (L) to day-10(R)

# optimal solution 

def minimum_days_to_make_m_bouquets(bloomdays,m,k):
    
    n = len(bloomdays)          # available no. of flowers currently 
    
    if m*k > n:                 # each bouquet has this many flowers if it is lessthan the available no. of flowers ==> return '-1'
        return -1
    
    def possible(min_days):               #  How many bouquets can I make using flowers that have bloomed by this day?
        
        bouquets_possible = 0           # bouquets possible initially is '0'
        flowers = 0                         # flowers isn't bloomed initially is '0'
        
        for bloom in bloomdays:
            if bloom <= min_days:           # this condition tell's us that is this flower is bloomed at this day if yes continue the if block code 
                
                flowers += 1                # increament the flowers 
                if flowers == k:                    # when flowers exactly equal to k then we can make the boquet
                    bouquets_possible += 1
                    flowers = 0                 # again make the flowers = 0 why ?? ==> now for the next bouquet you have to place the flowers 
            
            else:                           #{VVVVIMP}
                flowers = 0                         # flowers = 0 i.e why ?? what if the flowers isn't bloomed in a order {refer the book} i.e [T,T,F,T,T] (flowers bloomed order)
                                                        # here assume the previous flower count = 3 and now if condition is this flower is bloomed in this day if NO ==> if condition if false but in the memory previous flowers count is there which leads to wrong calculations
                                    # {VVVVVimp}       # if the next flower isn't bloomed in the next day we have to make the flowers = 0 
        
        return bouquets_possible >= m          #{in the question they says indirectly atleast keyword refer in leetcode }     # here boquets done >= m .... why ?? in the question { can i make ATLEAST 'M' bouquets is the question} 

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

# [1,10,3,10,2]  here actually the array says like the          {index = flower, value = day }
# first flower blooms in day 1 
#  second flower blooms in day 10 
#  third flower blooms in day 3
#  fourth flower blooms in day 10
# fith flower blooms in day 2 

# that means all flowers will be bloomed by the day 10 

# {VVVVIMP}     at every step think like is this flower is bloomed at this day or not ? if yes if condition inside logic execute 

# {question meaning} 
#  here we have to find the can i make this much of boquets_needed if question is asked this much of bouquets (bouquets_needed >= m)

# and also question says that in this days the flowers are bloomed are not {refer the above starting comments section here}



