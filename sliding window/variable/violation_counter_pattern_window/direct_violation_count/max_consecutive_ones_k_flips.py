#brute force
def max_consective_ones_k_flips(arr,k):
    n = len(arr)
    max_len = 0
    for i in range(n):
        zero_count = 0
        
        for j in range(i,n):
            if arr[j] == 0:
                zero_count += 1
                
            if zero_count <= k:
                max_len = max(max_len,j-i+1)
    return max_len
print(max_consective_ones_k_flips([1,1,1,0,0,0,1,1,1,1,0],2))   #6


#optimal solution 

def max_consective_one_k_flips(arr,k):
    
    l = 0
    zero_count = 0
    
    max_len = 0
    
    for r in range(len(arr)):
        
        if arr[r] == 0:
            zero_count +=1
        
        while zero_count > k:
            
            if arr[l] == 0:
                zero_count -=1
            
            l += 1
        max_len = max(max_len,r-l+1)
        
    return max_len
    
    
print(max_consective_one_k_flips([1,1,1,0,0,0,1,1,1,1,0],2))  #6