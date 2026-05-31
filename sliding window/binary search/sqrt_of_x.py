

# this is the question we have to find the square root of x i.e sqrt(36) = 6 

#  here the search space is l and r 
#  l = 1 because of sqrt(36) the minimum val is 1 i.e the sqrt(36) min_val can be 1 only
#  and max_val cannt be execced the 36 
#  the search space is 1 to 36 ==> l = 1 and r = 36 
#  here for the mid value ==> we calculate the square of mid why ?? 1 to 36 which gives the mid value in this range only 

#  square of mid  = mid * mid 

# if square of mid > x then r = mid - 1
# other wise l = mid + 1 

#   {VVVVVV IIMPP}
# here we must be assign ans = 0 because if sqrt(10) if ans = 0 not be assigned then it can't be calculate the sqrt(10) value 

# to cover that edge case wew must keep the ans = 0 to calculate the sqrt() of non-perfect squares 

# optimal solution 

def sqrt_of_x(x):
    
    l = 1
    r = 36
    ans = 0             # we must keep the ans = 0 to calculate the sqrt() of non-perfect squares 

    while l <= r:                       # the below line is important
        mid = l + (r-l)//2          #  1 to 36 =. mid = 6 then sqrt(36) = mid = 6 so only the mid = answer here the mid is not equal to index position okk important 
        
        square = mid * mid
        if square == x:
            return mid 
        
        elif square > x:
            ans = mid 
            r = mid - 1
            
        elif square < x:
            ans = mid 
            l = mid + 1
    return ans
print(sqrt_of_x(36))

print(sqrt_of_x(25))
print(sqrt_of_x(10))