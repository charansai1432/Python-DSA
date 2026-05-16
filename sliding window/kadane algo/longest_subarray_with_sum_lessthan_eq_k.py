# brute force approach 

def longest_subarray_with_sum_lessthan_k(arr,k):
    max_len = 0
    
    n = len(arr)
    
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            if cur_sum <= k:
                max_len = max(max_len,j-i+1)
    return max_len
print(longest_subarray_with_sum_lessthan_k([2,2,-1],3))


# here the optimal solution we have to solve this question using the prefix + Binary search + kadane's algo 

# the TC=> O(n log n ) due to binary search 
import bisect
def longest_subarray_with_sum_lessthan_eq_k(arr,k):
    
    prefix = 0
    max_len = 0
    
    sorted_prefix = [(0,-1)]            # storing the prefix_sum to index position in sorted_prefix
    
    for i , num in enumerate(arr):      # Get the index and number from the array
        prefix += num 
        
        target = prefix - k             # same as the maximum sum subarray of sum <= k 
                                        # in simple terms minimum prefix we need == target 
                                        
        bisect.insort(sorted_prefix,(prefix,i))             # store current prefix + index in the sorted_prefix
        
        for p,idx in sorted_prefix:     # find first_prefix >= target
            
            if p >= target:
                cur_len = i - idx 
                max_len = max(max_len,cur_len) #length = current index - previous index 
                break                         #why break ??        # sorted_prefix is sorted i.e first_valid_prefix is found == best choice
        
         
    return max_len
print(longest_subarray_with_sum_lessthan_eq_k([2,2,-1],3))
        


# ooptimal solution 


def longest_subarray_with_sum_lessthan_eq_k(arr,k):
    max_len = 0
    cur_prefix = 0
    n = len(arr)
    sorted_past_prefix_records = [(0,-1)]
    for i in range(n):
        cur_prefix += arr[i]
        target = cur_prefix - k
        idx = bisect.bisect_left(sorted_past_prefix_records,(target,float('-inf')))
        bisect.insort(sorted_past_prefix_records,(cur_prefix,i))
        if idx < len(sorted_past_prefix_records):
            past_prefix,past_idx = sorted_past_prefix_records[idx]
            cur_len = i - past_idx
            max_len = max(max_len,cur_len)
    return max_len
print(longest_subarray_with_sum_lessthan_eq_k([2,2,-1],3))
        
