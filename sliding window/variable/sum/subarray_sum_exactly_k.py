#brute force approach 

def subarray_sum_exactly_k(arr,k):
    
    max_len = 0
    n = len(arr)
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            
            if cur_sum == k:
                max_len = max(max_len,j-i+1)
    return max_len    
print(subarray_sum_exactly_k([1,2,3,4,5],5)) #2

#optimal solution 

def subarray_sum_exactly_k(arr,k):
    
    n = len(arr)
    
    l = 0
    
    # result = []
    win_sum = 0
    max_len = 0
    for r in range(n):
        win_sum += arr[r]
        
        while win_sum > k:
            
            win_sum -= arr[l]
            l+=1
            
            if win_sum == k :
                max_len = max(max_len,r-l+1)
    return max_len

print(subarray_sum_exactly_k([1,2,3,4,5],5)) #2