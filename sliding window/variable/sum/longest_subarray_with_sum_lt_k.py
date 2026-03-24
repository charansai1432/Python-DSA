#brute force approach 

from collections import defaultdict

def longest_subarray_with_sum_lt_k(arr,k):
    
    max_len = 0
    n = len(arr)
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            if cur_sum <= k:
                max_len = max(max_len,j-i+1)
    return max_len
print(longest_subarray_with_sum_lt_k([2,1,3,2,4],5))  #2  




# optimal solution 

def longest_subarray_with_sum_lt_k(arr,k):
    
    left = 0
    
    max_len = 0
    win_sum = 0
    for r in range(len(arr)):
        win_sum += arr[r]
        
        while win_sum > k:
            win_sum -= arr[left]
            left +=1 
        max_len = max(max_len,r-left+1)
    return max_len
print(longest_subarray_with_sum_lt_k([2,1,3,2,4],5))  #2

