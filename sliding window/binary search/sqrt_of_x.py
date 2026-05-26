

# optimal solution 

def sqrt_of_x(x):
    
    l = 1
    r = 36
    ans = 0
    while l <= r:
        mid = l + (r-l)//2
        
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