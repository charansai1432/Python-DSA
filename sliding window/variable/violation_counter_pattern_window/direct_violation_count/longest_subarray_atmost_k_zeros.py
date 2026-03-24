#brute force approach

def longest_subarray_with_atmost_k_zeros(arr,k):
    
    n = len(arr)
    max_len = 0
    # zero_count = 0
    for i in range(n):
        zero_count = 0
        for j in range(i,n):
            if arr[j] == 0:
                zero_count += 1
            if zero_count <= k:
                max_len = max(max_len,j-i+1)
    return max_len
print(longest_subarray_with_atmost_k_zeros([0,0,1,1,1,0,0],2))  # 5


#optimal solution 

def longest_subarray_with_atmost_k_zeros(arr,k):
    
    
    max_len = 0
    
    zero_count = 0
    
    l = 0 
    
    for r in range(len(arr)):
        
        if arr[r] == 0:
            zero_count += 1
            
        while zero_count > k:
            if arr[l] == 0:
                zero_count -= 1
                
            l += 1
            
        if (r-l+1) > max_len:
            max_len = r -l +1
            start = l
            
            
        max_len = max(max_len,r-l+1)
    return max_len,arr[start:start+max_len]
print(longest_subarray_with_atmost_k_zeros([0,0,1,1,1,0,0],2))  #5