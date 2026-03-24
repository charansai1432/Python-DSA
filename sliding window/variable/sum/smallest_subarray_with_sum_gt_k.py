# brute force approach

from collections import defaultdict
def smallest_subarray_with_gt_k(arr,k):
    
    n = len(arr)
    min_len = float('inf')
    
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            
            if cur_sum >= k:
                min_len = min(min_len,j-i+1)
    return min_len

print(smallest_subarray_with_gt_k([2,3,1,2,4,3],7))  #2


#optimal solution

def smallest_subarray_with_sum_gt_k(arr,k):
    
    min_len = float('inf')
    
    win_sum = 0
    
    l = 0
    
    for r in range(len(arr)):
        
        win_sum += arr[r]
        
        while win_sum >= k:
            
            min_len = min(min_len,r-l+1)
            
            win_sum -= arr[l]
            
            l += 1
    return min_len
print(smallest_subarray_with_sum_gt_k([2,3,1,2,4,3],7))  #2